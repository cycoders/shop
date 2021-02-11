from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from product.models import Product


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=False)
    verify_status = models.BooleanField(null=False)
    body = models.TextField()
    image = models.ImageField(upload_to='banner/static/images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
