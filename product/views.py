from django.shortcuts import render, redirect,get_object_or_404
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
    return render(request, 'store/add_product.html', {'form': form})

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
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id, owner=request.user)
    
    if request.method == 'POST':
        product.delete()
        # messages.success(request, f'Product "{product.name}" has been deleted successfully.')
        return redirect('product_list')
    
    return render(request, 'store/confirm_delete_product.html', {'product': product})

@login_required
def product_list(request):
    products = Product.objects.filter(owner=request.user)
    return render(request, 'store/product.html', {'products': products})