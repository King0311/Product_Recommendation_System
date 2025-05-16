from .models import *
from rest_framework import serializers

class Product_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

    def validate(self, data):
        price = data.get("price")
        if price <= 0:
            raise serializers.ValidationError("Price must be greater than 0")
        return data
    
class Order_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"