# import libraries
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage

# app-related imports
from photostore.models import Product, Cart
from photostore.forms import SearchForm
from .util import paginate, get_theme_code


# HOME views
def index(request):
    if request.user.is_authenticated:        
        fname = f"{request.session.get('first_name')}".capitalize() 
        lname = f"{request.session.get('last_name')}".capitalize()
        context = {
            "message" : f"{fname} {lname}! Welcome to PG's Picsies!",
        }
        return render(request, 'photostore/index.html', context) 
    
    # if user not authenticated
    else:
        return render(request, 'photostore/index.html') 
 

def search(request):
    # django SearchForm removed, to reduce complexity
  
    # collect search terms and filter 'Product' 
    query = request.GET.get('query')
    search_results = []

    search_results = Product.objects.filter(description__icontains=query) | Product.objects.filter(title__icontains=query)

    if search_results:
        context = {
                "query" : query,
                "search_results" : search_results,
                }
        return render(request, 'photostore/search.html', context)            
    else:
        context = {
            "query" : str(query).capitalize(),
        }
        return render(request, 'photostore/not_found.html', context)



# PRODUCTS views
def products(request):
    # define pagination terms
    items_per_page = 12
    all_products = Product.objects.all()
    page_content = paginate(request, products_list=all_products, items_per_page=items_per_page)

    context = {
        "all_products": page_content,
            }
    return render(request, 'photostore/products.html', context)


def filter_products(request):
    category_selected = request.GET.get('category')
    theme_selected = request.GET.get('theme')
    author_selected = request.GET.get('author')

    selected_theme_code = get_theme_code(theme_selected)
    filtered_products = Product.objects.filter(category__icontains=category_selected) | Product.objects.filter(theme=selected_theme_code) | Product.objects.filter(author=author_selected)

    # items_per_page = 6
    # page_content = paginate(request, products_list=filtered_products, items_per_page=items_per_page)

    context = {
        "category_selected": category_selected,
        "theme_selected": theme_selected,
        "author_selected": author_selected,
        "filtered_products": filtered_products,        
    }
    return render(request, 'photostore/products.html', context)



# CHECKOUT views
from django.http import JsonResponse

def add_to_cart(request, product_id):
    request.session['product_added'] = True
    item_to_add = Product.objects.get(id=product_id)
    
    # insert data to Cart model
    cart_item = Cart()
    cart_item.item = item_to_add
    cart_item.quantity = 2 # hard-coded for functionality test
    cart_item.save()
     
    context = {
        'cart' : Cart.objects.all(),
        }
    return render(request, 'photostore/cart.html', context)


def checkout(request):
    return render(request, 'photostore/checkout.html')


def payment(request, choice):
    context = {
        'choice' : choice,
    }
    return render(request, 'photostore/payment.html', context)



# OTHER views
def about_us(request):
    return render(request, 'photostore/about_us.html')

def license(request):
    return render(request, 'photostore/license.html')
