from django.db import models
from django.contrib.auth.models import AbstractUser,Group, Permission
from django.utils.translation import gettext as _

# Create your models here.
class SellerUser(AbstractUser):
    username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
    email = models.EmailField(unique = True)
    password = models.CharField(max_length=255)
    fullname=   models.CharField(max_length = 50)
    phonenumber= models.CharField(max_length=10)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    role = models.CharField(max_length=10)

    address = models.CharField(max_length=255)
    bio = models.CharField(max_length=255,blank=False,default="")
     
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS =[email,password,fullname,phonenumber,role,address]
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_('The groups this seller belongs to.'),
        related_name='seller_users_groups'  # Custom related_name to avoid clashes
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this seller.'),
        related_name='seller_users_permissions'  # Custom related_name to avoid clashes
    )

    def __str__(self):
        return self.email 