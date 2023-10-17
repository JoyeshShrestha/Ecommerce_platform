from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
    email = models.EmailField(unique = True)
    password = models.CharField(max_length=255)
    fullname=   models.CharField(max_length = 50)
    phonenumber= models.CharField(max_length=10)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)


    address = models.CharField(max_length=255)
    bio = models.CharField(max_length=255,blank=False,default="")
     
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS =[email,password,fullname,phonenumber,address]
