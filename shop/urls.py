from django.urls import path
from .views import shop_view, product_view, add_to_cart, remove_from cart

urlpatterns = [
    path('', shop_view, name='shop'),
    path('<int:product_id>/', product_view, name='product'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
]

