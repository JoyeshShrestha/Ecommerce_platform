from django.contrib import admin
from django.urls import path, include
from .views import GetAllItemsView,SpecificItemsViewByName
from reviews.views import ReviewView



urlpatterns = [
    path('', GetAllItemsView.as_view()),
    path('search/', SpecificItemsViewByName.as_view(),name='specific-items-by-name'),
    path('review/', ReviewView.as_view(),name='specific-items-review'),

    
    

    
]