from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .models import Product, ProductType, Department
from .serializers import ProductSerializer, ProductTypeSerializer, DepartmentSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
# Create your views here.

class ProductApiView(ModelViewSet): #modelviewset have all the logic about crud operations
    queryset = Product.objects.all()
    serializer_class = ProductSerializer # it helps to response 
    permission_classes = [IsAuthenticated] # it helps to authenticate the user


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
    
class DepartmentApiView(GenericViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def list(self, request):
        department_obj = self.get_queryset()
        serializer = self.get_serializer(department_obj, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    def retrieve(self, request, pk):
        department_obj = self.get_object()
        serializer = self.get_serializer(department_obj)
        return Response(serializer.data)
    
    def update(self, request, pk):
        department_obj = self.get_object()
        serializer  = self.get_serializer(department_obj, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def partial_update(self, request, pk):
        department_obj = self.get_object()
        serializer = self.get_serializer(department_obj, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
    def destroy(self, request, pk):
        department_obj = self.get_object()
        department_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def register_api_view(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        user.set_password(user.password)
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)