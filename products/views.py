# views.py
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from django.http import JsonResponse
from django.views import View
from .models import Products
from .serializers import ProductsSerializer
from reviews.serializers import ReviewsSerializer
from registration.models import User
import jwt
from reviews.models import Review


class GetAllItemsView(View):
    def get(self, request, *args, **kwargs):
        items = Products.objects.all()
        
        # Serialize the items using the ItemListingSerializer
        serializer = ProductsSerializer(items, many=True)

        # Return the serialized items as JSON response
        response_data = {
             "All products": serializer.data,
            
        }
        return JsonResponse(serializer.data, safe=False)
    
    
        
class SpecificItemsViewByName(View):
    #search item by name
    def post(self, request, *args, **kwargs):
    
        search_name = request.POST.get('name')

        items = Products.objects.filter(name = search_name).first()


        # Return the serialized items as JSON response
        # return Response(items)
        if items:
            # Serialize the item using the ProductsSerializer
            
            serializer = ProductsSerializer(items)
            review = Review.objects.filter(product = items.id ).all()
            
        # Serialize the review using the ReviewsSerializer
            if review is None:
                 response_data = {
                    "Product": serializer.data,
                    "Reviews": review  # Access the serialized data
                }
            else:     
                review_serializer = ReviewsSerializer(review,many=True)  # Provide data to validate

                # if review_serializer.is_valid():
                #     review_serializer.save()

                response_data = {
                    "Product": serializer.data,
                    "Reviews": review_serializer.data  # Access the serialized data
                }
            return JsonResponse(response_data, safe=False)
            
        else:
    # Handle the case when the item is not found
            return JsonResponse({'message': 'Item not found'}, status=404)

