from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Product
from .serializers import ProductSerializer

# Create your views here.

class ProductApiView(ModelViewSet): #modelviewset have all the logic about crud operations
    queryset = Product.objects.all()
    serializer_class = ProductSerializer # it helps to response 