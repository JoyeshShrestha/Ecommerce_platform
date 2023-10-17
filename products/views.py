# views.py

from rest_framework import viewsets
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from django.http import JsonResponse
from django.views import View
from .models import Products
from .serializers import ProductsSerializer

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



