# import libraries
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# app-related imports
from photostore.models import Product
from photostore.forms import SearchForm

# Global variables
import random

# collect all themes
theme_choices = Product.THEME_CHOICES
theme_codes = [theme[0] for theme in theme_choices]
theme_names = [theme[1] for theme in theme_choices]

# 'Theme of the Day' section
# Random Theme label
theme_index = random.choice(range(len(theme_choices)))
theme_label = theme_names[theme_index]

# Randomized Theme pictures
theme_count = 9    # homepage display
# filter based on chosen theme_label
theme_set = Product.objects.filter(theme=theme_codes[theme_index])   
rand_theme_inds = random.choices(range(theme_set.count()), k=theme_count)
# collect random theme images using randomized indices
rand_theme_pics = [theme_set[ind] for ind in rand_theme_inds]    


# randomize themes for 'Photo' and 'Art' of the day pictures
# filter by categoy
photos = Product.objects.filter(category='PH')
art = Product.objects.filter(category='ART')

# randomize and pick image
rand_photo_ind = random.choice(range(photos.count()))
rand_photo = photos[rand_photo_ind]

rand_art_ind = random.choice(range(art.count()))
rand_art = art[rand_art_ind]


# HOME views
def index(request):
    if request.user.is_authenticated:        
        fname = f"{request.session.get('first_name')}".capitalize() 
        lname = f"{request.session.get('last_name')}".capitalize()
        context = {
            "message" : f"{fname} {lname}! Welcome to PG's Picsies!",
            "random_photo" : rand_photo,
            "random_art" : rand_art,
            "theme_label" : theme_label,
            "theme_pictures" : rand_theme_pics,
        } 
    
    # if user not authenticated
    else:
        context = {
            "random_photo" : rand_photo,
            "random_art" : rand_art,
            "theme_label" : theme_label,
            "theme_pictures" : rand_theme_pics,
        } 

    return render(request, 'photostore/index.html', context)



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
# Variable relevant to PRODUCT Views
# define pagination terms
items_per_page = 12
all_products = Product.objects.all()
paginator = Paginator(all_products, items_per_page)

# dropdown filter options
categories = [category[1] for category in Product.CATEGORY_CHOICES]
authors = Product.objects.values_list('author', flat=True).distinct()

def products(request):
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

    context = {
        "all_products": content_page,
        "random_photo": rand_photo,
        "random_art": rand_art,
        "categories" : categories,
        "themes" : theme_names,
        "authors" : authors,
             }
    return render(request, 'photostore/products.html', context)

def filter_products(request):
    category_selected = request.GET.get('category')
    theme_selected = request.GET.get('theme')
    author_selected = request.GET.get('author')

    # rewire theme_selected to theme_code
    selected_theme_code = theme_codes[theme_names.index(theme_selected)]
    filtered_products = Product.objects.filter(category__icontains=category_selected) | Product.objects.filter(theme=selected_theme_code) | Product.objects.filter(author=author_selected)

    context = {
        "random_photo": rand_photo,
        "random_art": rand_art,
        "categories" : categories,
        "themes" : theme_names,
        "authors" : authors,
        "category_selected": category_selected,
        "theme_selected": theme_selected,
        "author_selected": author_selected,
        "filtered_products": filtered_products,        
    }
    return render(request, 'photostore/products.html', context)



# CHECKOUT views
def checkout(request):
    return render(request, 'photostore/checkout.html')

def payment(request, choice):
    return render(request, 'photostore/payment.html', context={
        "choice": choice,
    })



# OTHER views
def about_us(request):
    return render(request, 'photostore/about_us.html')

def license(request):
    return render(request, 'photostore/license.html')
