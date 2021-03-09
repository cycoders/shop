from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product
# Create your views here.


def create(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    return render(request, 'product/create.html')


def product_read(request):
        products = Product.objects.all()
        return render(request, 'product/show_product.html', {'products': products})


def product_delete(request, id):
    products = Product.objects.get(id=id)
    products.delete()
    return redirect('product/show_product.html')

def update(request, id):

    if request.user.has_perm("course.change_course"):
        products = Product.objects.get(id=id)
        if request.method == "POST":
            form = ProductForm(request.POST, request.FILES, instance=products)
            if form.is_valid():
                form.save()
                return redirect('read.dashboard')
    else:
        return redirect('register')
    return render(request, 'products/update.html', {'products': products})