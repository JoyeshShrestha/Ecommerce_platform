from django.contrib import admin
from django.urls import path, include
from .views import ItemListingViewSet,GetAllItemsView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', ItemListingViewSet)

urlpatterns = [
    path('', GetAllItemsView.as_view()),
    path('dashboard/', include(router.urls)),
    

    
]