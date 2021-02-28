from django.shortcuts import render
from .forms import ProductForm
from .models import Product
# Create your views here.

def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
