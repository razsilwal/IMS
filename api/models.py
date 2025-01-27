from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=200, null=True)
    password = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    image = models.FileField(upload_to='media/user/')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    stock = models.IntegerField()
    description = models.TextField()
    type_id = models.ForeignKey('ProductType', on_delete=models.SET_NULL, null=True)
    department_id = models.ManyToManyField('Department')

class ProductType(models.Model):
    name = models.CharField(max_length=200)


class Department(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

class Purchase(models.Model):
    price = models.FloatField()
    quantity =  models.IntegerField()
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE) 
    vendor_id = models.ForeignKey('vendor', on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

class Sell(models.Model):
    price = models.FloatField()
    quantity =  models.IntegerField()
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE) 
    customer_name = models.CharField(max_length=200)
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


class Vendor(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    address = models.CharField(max_length=200)
    contact_no = models.CharField(max_length=200)
    email = models.EmailField()