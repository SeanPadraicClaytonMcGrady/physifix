from . import views
from django.urls import path

urlpatterns = [
    path("read_all", views.read_all, name="read_all")
]
