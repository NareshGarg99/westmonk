from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name = "store"),
    path('product-page/', views.product_page, name = "product-page"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name = "checkout")
]