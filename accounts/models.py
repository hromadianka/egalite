from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username

class Editor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    can_edit_about = models.BooleanField(default=False)
    can_manage_products = models.BooleanField(default=False)
    can_manage_orders = models.BooleanField(default=False)
    can_manage_publications = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username