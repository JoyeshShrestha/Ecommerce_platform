from rest_framework import serializers
from .models import Carts

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carts
        fields =  ['name', 'subprice', 'quantity', 'price'] 


        