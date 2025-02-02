"""
URL configuration for IMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api.views import ProductApiView, ProductTypeApiView, DepartmentApiView, register_api_view, login_api_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product-type/', ProductTypeApiView.as_view({'get':'list', 'post':'create'})), 
    path('product-type/<int:pk>/', ProductTypeApiView.as_view({'get':'retrieve', 'put':'update', 'patch':'partial_update', 'delete':'delete'})), 
    path('product/', ProductApiView.as_view({'get':'list', 'post':'create'})), 
    path('department/', DepartmentApiView.as_view({'get':'list', 'post':'create'})), 
    path('department/<int:pk>/', DepartmentApiView.as_view({'get':'retrieve', 'put':'update', 'patch':'partial_update', 'delete':'destroy'})), 
    path('product/<int:pk>/', ProductApiView.as_view({'get':'retrieve', 'put':'update', 'patch':'partial_update', 'delete':'destroy'})),
    path('register/', register_api_view), 
    path('login/', login_api_view), 
]
# pip freeze > requirements.txt'

# pip install -r requirement.txt

# git rm --cached env