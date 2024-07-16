from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.owner = request.user
            product.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'product/add_product.html', {'form': form})

@login_required
def edit_product(request, product_id):
    product = Product.objects.get(product_id=product_id, owner=request.user)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'product/edit_product.html', {'form': form})

@login_required
def product_list(request):
    products = Product.objects.filter(owner=request.user)
    return render(request, 'product/product_list.html', {'products': products})