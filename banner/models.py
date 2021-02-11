from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Banner(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.DecimalField(max_digits=4, decimal_places=4)
    title = models.CharField(max_length=50, null=False)
    image = models.ImageField(upload_to='banner/static/images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)