# views.py
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import viewsets
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from django.http import JsonResponse
from django.views import View
from .models import Products
from .serializers import ProductsSerializer
from registration.models import User
import jwt

class ItemListingViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

class GetAllItemsView(View):
    def get(self, request, *args, **kwargs):
        items = Products.objects.all()

        # Serialize the items using the ItemListingSerializer
        serializer = ProductsSerializer(items, many=True)

        # Return the serialized items as JSON response
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
            return JsonResponse(serializer.data, safe=False)
        else:
            # Handle the case when the item is not found
            return JsonResponse({'message': 'Item not found'}, status=404)
    