from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .models import Product, ProductType
from .serializers import ProductSerializer, ProductTypeSerializer
from rest_framework.response import Response

# Create your views here.

class ProductApiView(ModelViewSet): #modelviewset have all the logic about crud operations
    queryset = Product.objects.all()
    serializer_class = ProductSerializer # it helps to response 

class ProductTypeApiView(GenericViewSet): # custom response logic 
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer


    # @property
    def list(self, request):
        product_type_obj = self.get_queryset()
        serializer = self.get_serializer(product_type_obj, many=True)
        return Response(serializer.data)