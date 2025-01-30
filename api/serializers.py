from rest_framework import serializers
from .models import Product, ProductType, Department, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password','email','image']

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
        