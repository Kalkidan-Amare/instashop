from django.contrib.auth.models import AbstractUser
from django.db import models
from template.models import Template

class User(AbstractUser):
    store_name = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=20, blank=True)
    is_seller = models.BooleanField(default=False)
    template = models.ForeignKey(Template, on_delete=models.SET_NULL, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.store_name:
            self.store_name = self.username
        super().save(*args, **kwargs)