from django.shortcuts import render
from .models import Product

# Create your views here.

def shop_view(request):
    products = Product.objects.all()  
    return render(request, 'shop/shop.html', {'products': products})

def product_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'shop/product.html', {'product': product})