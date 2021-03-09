from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'brand', 'seller', 'price', 'image', 'colors', 'serial', 'body']
