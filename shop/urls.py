
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product-View/', views.productView, name='productView'),
    path('tracking/', views.tracking, name='tracking'),
    path('checkout/', views.tracking, name='tracking'),
    path('cart/', views.cart, name='cart'),
]
