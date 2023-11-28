from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group, Permission


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
    

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100, default="")
    last_name = models.CharField(max_length=100, default="")
    bookmarks = models.ManyToManyField(Diagnostic)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    
    groups = models.ManyToManyField(Group, blank=True, related_name='user_custom_groups') 
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='user_custom_permissions')
    
    class Meta:
        app_label = 'server'
    
    
    