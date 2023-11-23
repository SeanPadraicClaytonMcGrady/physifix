from django.db import models


class Diagnostic(models.Model):
    name = models.CharField(max_length=100)
    video = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    region = models.ForeignKey('Region', on_delete=models.CASCADE)

class Region(models.Model):
    name = models.CharField(max_length=100)
    

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    bookmarks = models.ManyToManyField(Diagnostic)