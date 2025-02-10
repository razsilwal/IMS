from rest_framework import serializers
from .models import Product, ProductType, Department, User, Purchase, Sell, Vendor
from django.contrib.auth.models import Group

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password','email','image','groups']

    # def validate(self, attrs): if we want to customize the error
    #     attrs.get('phone_number')
    #     raise serializers.ValidationError('phone number error')
    #     return super().validate(attrs)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = '__all__'
    

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Group
        fields = ['id','name']   


class SellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sell
        fields = '__all__'

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        models = Vendor
        fields = '__all__'