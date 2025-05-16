from . import views
from django.urls import path, include
from rest_framework import routers


urlpatterns = [
    path("get_product/", views.get_product),
    path("get_product/<int:id>/", views.get_product),
    path("insert_product/", views.insert_product),
    path("update_product/<int:id>/", views.update_product),
    path("delete_product/<int:id>/", views.delete_product),
    #############################################################
    path("get_order/", views.get_order),
    path("get_order/<int:id>/", views.get_order),
    path("insert_order/", views.insert_order),
    path("update_order/<int:id>/", views.update_order),
    path("delete_order/<int:id>/", views.delete_order),
    #############################################################
    path("recommend_products/<int:id>", views.recommend_products),
    
]
