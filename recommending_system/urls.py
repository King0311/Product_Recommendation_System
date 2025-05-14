from . import views
from django.urls import path, include
from rest_framework import routers


urlpatterns = [
    path("get_product/", views.get_product),
    path("get_product/<int:id>/", views.get_product),
    path("insert_product/", views.insert_product),
    path("update_product/<int:id>/", views.update_product),
    path("delete_product/<int:id>/", views.delete_product),
]
