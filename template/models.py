from django.db import models

# Create your models here.
from django.db import models

class Template(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # is_premium = models.BooleanField(default=False)

    def __str__(self):
        return self.name