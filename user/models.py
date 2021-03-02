from django.db import models

# Create your models here.


class Profile(models.Model):
    fname = models.CharField(max_length=50, null=False)
    lname = models.CharField(max_length=50, null=False)
    image = models.ImageField(upload_to='static/profile/images/')
    biography = models.TextField()
    age = models.CharField(max_length=20, null=False)
    email = models.CharField(max_length=20, null=False)
    phone = models.CharField(max_length=20, null=False)
    address = models.TextField()
    postcode = models.CharField(max_length=20, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
