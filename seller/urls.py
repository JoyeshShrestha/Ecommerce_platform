from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import SellerRegisterView, SellerLoginView, ItemListingViewSet
router = DefaultRouter()
router.register(r'', ItemListingViewSet)
urlpatterns = [
    path('register/', SellerRegisterView.as_view()),
    path('login/', SellerLoginView.as_view()),

    path('manage/', include(router.urls)),
    
]