from django.urls import path
from .views import shop_view, product_view

urlpatterns = [
    path('', shop_view, name='shop'),
    path('<int:product_id>/', product_view, name='product'),
]

