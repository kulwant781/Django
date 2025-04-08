
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product-view/<int:Pid>', views.productView, name='productView'),
    path('tracking/', views.tracking, name='tracking'),
    path('checkout/', views.checkout, name='checkout'),
    path('contant-us/', views.contact, name='contant'),
    path('about-us/', views.about, name='about'),
    path('thank-you', views.thank_you, name='thank_you'),
    path('checkout_ajax/', views.checkout_ajax, name='checkout_ajax'),
    path('apply_coupon/', views.apply_coupon, name='apply_coupon'),
    path('search/', views.pro_search, name='pro_search'),
]
