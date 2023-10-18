from django.contrib.auth.models import User
from .models import SellerUser 
from rest_framework import authentication
from rest_framework import exceptions

from rest_framework.exceptions import AuthenticationFailed
import jwt

class SellerLoginAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = request.COOKIES.get('seller_jwt')
       
        if not token:
            raise AuthenticationFailed('Unaunthenticated!')
            # return None
        try:
            payload = jwt.decode(token, 'secret_key', algorithms=['HS256'])

        
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unaunthenticated!')
        
        except jwt.DecodeError as e:
            # Print or log the error message for debugging purposes
            print(f"Token decode error: {e}")
            raise AuthenticationFailed(f'Token is invalid')
        
        member = SellerUser.objects.filter(id=payload['id']).first()
        
        if member is None:
            raise AuthenticationFailed('User not found')
        return (member, None)