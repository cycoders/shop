from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/profile/images/')
    age = models.CharField(max_length=20, null=False)
    phone1 = models.CharField(max_length=20, null=False)
    phone2 = models.CharField(max_length=20, null=False)
    address = models.TextField()
    postcode = models.CharField(max_length=20, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
