from django.shortcuts import render
from rest_framework import status
from rest_framework import viewsets

from .models import SellerUser
from rest_framework.views import APIView
import secrets
from products.models import Products
from products.serializers import ProductsSerializer
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime
from .authentication import SellerLoginAuthentication

class ItemListingViewSet(viewsets.ModelViewSet):
    authentication_classes = [SellerLoginAuthentication]

    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
# Create your views here.
class SellerRegisterView(APIView):
    # class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            response_data = {
                'username': user.username,
                'email': user.email,
                'fullname': user.fullname,
                'phonenumber': user.phonenumber,
                'role':user.role,
                'address':user.address,


            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class SellerLoginView(APIView):
    def post(self,request):
        email = request.data['email']
        password = request.data['password']

        seller = SellerUser.objects.filter(email=email).first()

        if seller is None:
            raise AuthenticationFailed('User not found!')
        
        if not seller.check_password(password.encode('utf-8')):
            
            raise AuthenticationFailed('Incorrect password!')
        
        payload = {
            'id' : seller.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes = 60),
            'iat': datetime.datetime.utcnow()
        }
        

        token = jwt.encode(payload, 'secret_key', algorithm = 'HS256')
        # decoded_payload = jwt.decode(token, 'secret_key', algorithms=['HS256'])
        
        response = Response()


        response.set_cookie(key='seller_jwt', value=token, httponly=True)
        response.data = {
                        'message' : token

        }
        
        
         
        
        
        return response
    