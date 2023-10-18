from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=255,null=False,unique=True)
    description = models.CharField(max_length=255,null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    image = models.ImageField(upload_to='item_images/', null=True, blank=True)
   
    def __str__(self):
        return self.name