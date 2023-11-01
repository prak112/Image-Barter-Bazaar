from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'photostore/index.html')


def products(request):
    return render(request, 'photostore/products.html')


def checkout(request):
    return render(request, 'photostore/checkout.html')


def about_us(request):
    return render(request, 'photostore/about_us.html')
