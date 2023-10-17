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
    def get(self, request, *args, **kwargs):
        # Retrieve the JWT from cookies
        jwt_token = request.COOKIES.get('jwt')

        if jwt_token:
            try:
                # Decode the JWT to access user information
                decoded_payload = jwt.decode(jwt_token, 'secret_key', algorithms=['HS256'])
                user_id = decoded_payload['id']
                
                # Add your logic to retrieve and return user-specific data here
                # For example:
                user = User.objects.get(id=user_id)
                user_data = {
                    'id': user.id,
                    'username': user.username,
                    # Add more user data fields as needed
                }
                
                return JsonResponse(user_data)
            except jwt.ExpiredSignatureError:
                return JsonResponse({'error': 'JWT has expired'}, status=401)
            except jwt.DecodeError:
                return JsonResponse({'error': 'Invalid JWT'}, status=401)
        else:
            return JsonResponse({'error': 'JWT not found'}, status=401)    


