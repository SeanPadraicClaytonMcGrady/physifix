from . import views
from graphene_django.views import GraphQLView
from django.urls import path
from .schema import schema

urlpatterns = [
    path("read_all_diagnostics", views.read_all_diagnostics, name="read_all_diagnostics"),
    path("read_all_regions", views.read_all_regions, name="read_all_regions"),
    path("read_all_users", views.read_all_users, name="read_all_users"),
    path('graphql/', GraphQLView.as_view(graphiql=True, schema=schema), name='graphql'),
    path("login", views.log_in, name="login"),
]
