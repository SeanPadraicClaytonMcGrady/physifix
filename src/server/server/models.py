from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group, Permission, AbstractUser


class Diagnostic(models.Model):
    name = models.CharField(max_length=100)
    video = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    region = models.ForeignKey('Region', on_delete=models.CASCADE)
    
    class Meta:
        app_label = 'server'

class Region(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        app_label = 'server'
    
    
class User(AbstractUser):
    bookmarks = models.ManyToManyField(Diagnostic)
    
    groups = models.ManyToManyField(Group, blank=True, related_name='user_custom_groups') 
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='user_custom_permissions')
    
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True, default='user_{id}')
    
    class Meta:
        app_label = 'server'