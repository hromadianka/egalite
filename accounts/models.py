from django.contrib.auth.models import User
from django.db import models
from shop.models import Product
from feed.models import Publication

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    saved_posts = models.ManyToManyField(Publication, blank=True)
    saved_products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return self.user.username
