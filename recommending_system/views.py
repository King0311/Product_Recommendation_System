from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

# CURD of Product Data

@api_view(['GET'])
def get_product(request,id = None):
    try:
        if id :
            all_Products = Product.objects.get(id = id)
            serializer = Product_Serializer(all_Products, many=False)
        else:
            all_Products = Product.objects.all()
            serializer = Product_Serializer(all_Products, many=True)
        if serializer.data:
            return Response(serializer.data)
        else:
            return Response({'error': 'No products found'})
    except Exception as e:
        return Response({"message": str(e)})

@api_view(['POST'])
def insert_product(request):
    try:
        serializers = Product_Serializer(data = request.data, many=True)
        if serializers.is_valid():
            serializers.save()
            return Response({'message': serializers.data})
        else:
            return Response({
                "message" : serializers.errors
            })
    except Exception as e:
        return Response({"message": str(e)})

@api_view(["PUT"])
def update_product(request,id):
    try:
        product_to_update = Product.objects.get(id=id)
        serializers = Product_Serializer(product_to_update, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response({'message': serializers.data})
        else:
            return Response({"message": serializers.errors})
    except Exception as e:
        return Response({"message": str(e)})

@api_view(["DELETE"])
def delete_product(request,id):
    try:
        product_to_delete = Product.objects.get(id=id)
        product_to_delete.delete()
        return Response({'message': 'Product deleted successfully'})
    except Exception as e:
        return Response({"message": str(e)})


# CURD of Order Data


@api_view(["GET"])
def get_order(request, id=None):
    try:
        if id:
            all_Orders = Order.objects.get(id=id)
            serializer = Order_Serializer(all_Orders, many=False)
        else:
            all_Orders = Order.objects.all()
            serializer = Order_Serializer(all_Orders, many=True)
        if serializer.data:
            return Response(serializer.data)
        else:
            return Response({"error": "No orders found"})
    except Exception as e:
        return Response({"message": str(e)})

@api_view(["POST"])
def insert_order(request):
    try:
        price = 0
        for item in request.data[0]["products"]:
            product_detial = Product.objects.get(id = item)
            price += float(product_detial.price)

        request.data[0]["total_price"] = str(price)
        serializers = Order_Serializer(data=request.data, many=True)
        if serializers.is_valid():
            serializers.save()
            return Response({"message": serializers.data})
        else:
            return Response({"message": serializers.errors})
    except Exception as e:
        return Response({"message": str(e)})

@api_view(["PUT"])
def update_order(request, id):
    try:
        price = 0
        for item in request.data["products"]:
            product_detial = Product.objects.get(id=item)
            price += float(product_detial.price)

        request.data["total_price"] = str(price)

        order_to_update = Order.objects.get(id=id)
        serializers = Order_Serializer(
            order_to_update, data=request.data, partial=True
        )
        if serializers.is_valid():
            serializers.save()
            return Response({"message": serializers.data})
        else:
            return Response({"message": serializers.errors})
    except Exception as e:
        return Response({"message": str(e)})

@api_view(["DELETE"])
def delete_order(request, id):
    try:
        order_to_delete = Order.objects.get(id=id)
        order_to_delete.delete()
        return Response({"message": "Order deleted successfully"})
    except Exception as e:
        return Response({"message": str(e)})
