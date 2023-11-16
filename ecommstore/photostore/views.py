# import libraries
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# import models
from photostore.models import Product

# Create your views here.
def index(request):
    if request.user.is_authenticated:        
        fname = f"{request.session.get('first_name')}".capitalize() 
        lname = f"{request.session.get('last_name')}".capitalize()
        context = {
            "message" : f"{fname} {lname}! Welcome to PG's Picsies!"
        }
        return render(request, 'photostore/index.html', context=context)

    else:
        return render(request, 'photostore/index.html')


def products(request):
    all_products = Product.objects.all()
    # context = {"all_products": all_products,} 
    #               "categories": categories, "themes": themes, "authors": authors}

    # define pagination terms
    items_per_page = 12
    paginator = Paginator(all_products, items_per_page)

    # current page number
    current_page = request.GET.get('page')

    try:
        # display page content
        content_page = paginator.page(current_page)
    except PageNotAnInteger:
        content_page = paginator.page(1)
    except EmptyPage:
        # display last page, if out of range
        content_page = paginator.page(paginator.num_pages)

    context = {"all_products": content_page,}
    return render(request, 'photostore/products.html', context)

# def search(request, query):
#     if request.method == "POST":
#         return render(request, 'search.html')
#     else:
#         return HttpResponseRedirect(reverse('index'))


def checkout(request):
    return render(request, 'photostore/checkout.html')
def payment(request, choice):
    return render(request, 'photostore/payment.html', context={
        "choice": choice,
    })


def about_us(request):
    return render(request, 'photostore/about_us.html')

def license(request):
    return render(request, 'photostore/license.html')
