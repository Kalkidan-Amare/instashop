from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_product, name='add_product'),
    path('edit/<slug:product_id>/', views.edit_product, name='edit_product'),
    path('list/', views.product_list, name='product_list'),
]