from django.contrib import admin
from django.urls import path, include
from .views import ItemListingViewSet,GetAllItemsView,SpecificItemsViewByName
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', ItemListingViewSet)

urlpatterns = [
    path('', GetAllItemsView.as_view()),
    path('search/', SpecificItemsViewByName.as_view(),name='specific-items-by-name'),

    path('dashboard/', include(router.urls)),
    

    
]