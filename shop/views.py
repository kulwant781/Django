from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def home(request):
    products = Product.objects.all()
    print(products)
    return render(request, 'shop/index.html', {'products': products})
#    return HttpResponse("Shop, Hello World!")

def cart(request):
    return HttpResponse("Cart View")

def productView(request):
    return HttpResponse("Product View")

def checkout(request):
    return HttpResponse("Checkout View")

def tracking(request):
    return HttpResponse("Tracking View")