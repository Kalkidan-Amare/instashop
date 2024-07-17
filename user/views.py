from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from .models import User
from .forms import CustomUserCreationForm
from template.models import Template
from product.models import Product
from order.models import Order


def logout_view(request):
    logout(request)
    return redirect('home')

def home(request):
    return render(request, 'landing_page.html')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.store_name = user.username
            user.save()
            login(request, user)
            return redirect('choose_template')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def dashboard(request):
    if request.user.is_seller:
        products = Product.objects.filter(owner=request.user)
        orders = Order.objects.filter(seller=request.user)
        return render(request, 'store/dashboard.html', {'products': products, 'orders': orders})
    else:
        return redirect('choose_template')

@login_required
def choose_template(request):
    templates = Template.objects.all()
    return render(request, 'choose_template.html', {'templates': templates})

@login_required
def purchase_template(request, template_id):
    template = get_object_or_404(Template, id=template_id)
    request.user.template = template
    request.user.is_seller = True
    request.user.save()
    return redirect('store_view', request.user.store_name)

def store_view(request, slug):
    store_owner = get_object_or_404(User, store_name=slug)
    products = Product.objects.filter(owner=store_owner)
    
    context = {'store_owner': store_owner, 'products': products}
    render_template = store_owner.template.name

    if request.user == store_owner:
        orders = Order.objects.filter(seller=store_owner)
        context['orders'] = orders
    
    return render(request, f'store_templates/{render_template}.html', context)

def product_detail(request, id):
    product = Product.objects.get(id=id)
    context = {'product':product}
    
    return render(request, 'store/product_detail.html', context)