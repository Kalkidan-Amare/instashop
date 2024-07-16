from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .models import Order
from product.models import Product

@require_POST
def create_order(request):
    product_id = request.POST.get('product_id')
    buyer_name = request.POST.get('buyer_name')
    buyer_phone = request.POST.get('buyer_phone')
    
    product = Product.objects.get(id=product_id)
    
    order = Order.objects.create(
        seller = product.owner,
        buyer_name=buyer_name,
        buyer_phone_number=buyer_phone,
        product=product
    )
    
    return JsonResponse({'message': 'Purchase completed'})

@login_required
def order_list(request):
    orders = Order.objects.filter(seller=request.user)
    return render(request, 'order_list.html', {'orders': orders})