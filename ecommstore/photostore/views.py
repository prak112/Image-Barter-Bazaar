# import libraries
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse



# Create your views here.
def index(request):
    return render(request, 'photostore/index.html')


def products(request):
    return render(request, 'photostore/products.html')

# def search(request, query):
#     if request.method == "POST":
#         return render(request, 'search.html')
#     else:
#         return HttpResponseRedirect(reverse('index'))


def checkout(request):
    return render(request, 'photostore/checkout.html')


def about_us(request):
    return render(request, 'photostore/about_us.html')

def license(request):
    return render(request, 'photostore/license.html')
