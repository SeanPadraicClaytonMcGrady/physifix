from . import views
from django.urls import path

urlpatterns = [
    path("read_all_diagnostics", views.read_all_diagnostics, name="read_all_diagnostics"),
    path("read_all_regions", views.read_all_regions, name="read_all_regions"),
    path("read_all_users", views.read_all_users, name="read_all_users"),
    path("signin", views.sign_in, name="signin"),
]
