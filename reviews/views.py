from django.shortcuts import render
from rest_framework.views import APIView
from .authentication import LoginAuthentication
from .serializers import ReviewsSerializer
from .models import Review
from django.http import JsonResponse

from products.models import Products

# Create your views here.
class ReviewView(APIView):
    authentication_classes = [LoginAuthentication]
    def post(self, request):
        written_review = request.POST.get('review')
        rating = request.POST.get('rating')
        product_name= request.POST.get('product_name')
        member = request.user

        


        product = Products.objects.filter(name=product_name).first()
        print(product)
        
        if product is None:
            return JsonResponse({"message": "Product not found"})

        serializer = ReviewsSerializer(data={
                'user': member.id,
                'product': product.id,
                'review': written_review,
                'rating': rating
            })
        

        
        if serializer.is_valid():
                # If the serializer is valid, save the data
                serializer.save()
        else:
                return JsonResponse(serializer.errors, status=400)
        
        response_data = {
            **serializer.data,
            "Message": "Review Successfully given!"

        }
        return JsonResponse(response_data, safe=False)
    def get(self, request):
        member = request.user
        Reviews = Review.objects.filter(user =member.id).all()

        # Serialize the items using the ItemListingSerializer
        serializer = ReviewsSerializer(Reviews, many=True)

        # Return the serialized items as JSON response
        return JsonResponse(serializer.data, safe=False)
    def delete(self, request):
        member = request.user
        product_name= request.POST.get('product_name')

        prod = Products.objects.filter(name = product_name).first()

        if prod is None:
            return JsonResponse({"message":f"No products found with the name of {product_name}"})

        
        is_review = Review.objects.filter(user=member.id, product=prod.id).first()
        if is_review is None:
            return JsonResponse({"message":f"No REVIEW found with the name of {product_name}"})

        
        Review.objects.filter(user=member.id, product=prod.id).delete()


        # Serialize the items using the ItemListingSerializer
        

        # Return the serialized items as JSON response
        return JsonResponse({"message":f"successfully delete your review of {product_name}"})