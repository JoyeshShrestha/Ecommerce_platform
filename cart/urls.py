from django.contrib import admin
from django.urls import path, include
from .views import CartView, DeleteallView
urlpatterns = [
    path('', CartView.as_view()),
    path('empty/', DeleteallView.as_view()),

    

    
]