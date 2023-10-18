from django.shortcuts import render
from rest_framework.views import APIView
from products.models import Products
from .models import Carts
from rest_framework.exceptions import AuthenticationFailed
from .serializers import CartSerializer
from django.http import JsonResponse

# Create your views here.
class CartView(APIView):
    def get(self, request):
        all_carts = Carts.objects.all()
        
        if not all_carts:
            return JsonResponse({"message": "Your cart is empty"})
        serializer = CartSerializer(all_carts, many=True)
        all_prices = [cart.price for cart in all_carts]
        total_price = sum(all_prices)

        response_data = {
            "YourCart": serializer.data,
            "Total Price": total_price
        }

        return JsonResponse(response_data, safe=False)
    def post(self, request):
        product_name = request.data['name']
        quantity = request.data['quantity']
        product = Products.objects.filter(name=product_name).first()

        if product is None:
            raise AuthenticationFailed('Product not found!')
        similar_item = Carts.objects.filter(name=product_name).first()

        if similar_item:
            similar_item.quantity += quantity
            similar_item.price = product.price * similar_item.quantity
            similar_item.save()
            serializer = CartSerializer(similar_item)
        else:
            serializer = CartSerializer(data={
                'name': product_name,
                'subprice': product.price,
                'quantity': quantity,
                'price': product.price * quantity
            })

            if serializer.is_valid():
                # If the serializer is valid, save the data
                serializer.save()
            else:
                return JsonResponse(serializer.errors, status=400)  # Return validation errors

        all_carts = Carts.objects.all()
        
        if not all_carts:
            return JsonResponse({"message": "Your cart is empty"})

        # Extract all the prices from the Cart instances
        all_prices = [cart.price for cart in all_carts]
        total_price = sum(all_prices)

        response_data = {
            **serializer.data,
            "Message": "Successfully Added"

        }

        return JsonResponse(response_data, safe=False)
    
    def delete(self,request):
            product_name_to_delete = request.data.get('name')

            # Filter the cart items by name and delete them
            Carts.objects.filter(name=product_name_to_delete).delete()

            return JsonResponse({"message": f"Items with the name '{product_name_to_delete}' have been deleted from the cart"})
    

class DeleteallView(APIView):
    
        def delete(self,request):
            
            # Filter the cart items by name and delete them
            Carts.objects.all().delete()

            return JsonResponse({"message": "All items have been deleted"})