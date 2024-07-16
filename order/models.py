from django.db import models
from user.models import User
from product.models import Product

class Order(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sales')
    buyer_name = models.CharField(max_length=100)
    buyer_phone = models.CharField(max_length=20)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.buyer_name}"