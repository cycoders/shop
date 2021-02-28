from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Product(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=False)
    brand = models.CharField(max_length=50, null=False)
    seller = models.CharField(max_length=50, null=False)
    price = models.CharField(max_length=20, null=False)
    image = models.ImageField(upload_to='static/product/images/')
    colors = models.CharField(max_length=20, null=False)
    serial = models.CharField(max_length=10, null=False, unique=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#class ProductProperties(models.Model):
    #product = models.ForeignKey(Product, on_delete=models.CASCADE)
    #image = models.ImageField('product/static/images/')
    #created_at = models.DateTimeField(auto_now_add=True)
    #updated_at = models.DateTimeField(auto_now=True)



