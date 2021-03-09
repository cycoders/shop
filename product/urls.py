<<<<<<< HEAD
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    
]
=======
from django.urls import path
from . import views

urlpatterns = [
    path('create', views.product_create, name='product.create'),
    path('read', views.product_read, name='product.read'),
    path('delete/<int:id>', views.product_delete, name='product.delete'),


    ]
>>>>>>> product
