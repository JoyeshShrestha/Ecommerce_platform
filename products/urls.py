from django.contrib import admin
from django.urls import path, include
from .views import ItemListingViewSet,GetAllItemsView,SpecificItemsViewByName
from rest_framework.routers import DefaultRouter
from reviews.views import ReviewView

router = DefaultRouter()
router.register(r'', ItemListingViewSet)

urlpatterns = [
    path('', GetAllItemsView.as_view()),
    path('search/', SpecificItemsViewByName.as_view(),name='specific-items-by-name'),
    path('review/', ReviewView.as_view(),name='specific-items-review'),

    path('dashboard/', include(router.urls)),
    
    

    
]