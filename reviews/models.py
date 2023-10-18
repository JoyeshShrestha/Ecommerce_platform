from django.db import models
from registration.models import User
from products.models import Products

# Create your models here.
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Relationship to the User model
    product = models.ForeignKey(Products, on_delete=models.CASCADE)  # Relationship to the Product model
    review = models.CharField(max_length=255)
    rating = models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])