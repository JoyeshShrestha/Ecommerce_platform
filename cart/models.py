from django.db import models

# Create your models here.
class Carts(models.Model):
    name = models.CharField(max_length=255,null=False)
    subprice =models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    quantity = models.IntegerField(max_length=2, default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
