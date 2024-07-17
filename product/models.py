from django.db import models
from django.utils.text import slugify
from user.models import User

class Product(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='image/')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    product_id = models.SlugField(max_length=255, unique=True, blank=True)
    stock = models.IntegerField(null=True,blank=True, default=1)

    def save(self, *args, **kwargs):
        if not self.product_id:
            store_name = self.owner.store_name if hasattr(self.owner, 'store_name') else self.owner.username
            self.product_id = slugify(f"{store_name}-{self.name}")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'

    def get_total_price(self):
        return self.quantity * self.product.price