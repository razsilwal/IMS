from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .models import Product, ProductType
from .serializers import ProductSerializer, ProductTypeSerializer
from rest_framework.response import Response
from rest_framework import status

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
    
    def create(self, request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk):
        # try: 
        #     product_type_obj = ProductType.objects.get(id=pk)
            
        # except:
        #     return Response({"detail":"Data not found"}, status=status.HTTP_404_NOT_FOUND)
        product_type_obj = self.get_object()
        serializer = self.get_serializer(product_type_obj)
        return Response(serializer.data)
    
    def update(self, request, pk):
        product_type_obj = self.get_object() 
        serializer = self.get_serializer(product_type_obj, data=request.data) #obj data and request data help to update  the database
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def partial_update(self, request, pk):
        product_type_obj = self.get_object()
        serializer = self.get_serializer(product_type_obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product_type_obj = self.get_object()
        product_type_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)