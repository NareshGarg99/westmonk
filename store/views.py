from django.shortcuts import render

# Create your views here.
def store(request):
    data = {}
    return render(request, 'store/store.html', data)

def checkout(request):
    data = {}
    return render(request, 'store/checkout.html', data)

def cart(request):
    data = {}
    return render(request, 'store/cart.html', data)

def product_page(request):
    data = {}
    return render(request, 'store/product_page.html', data)