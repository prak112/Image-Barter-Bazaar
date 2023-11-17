# import libraries
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# import models
from photostore.models import Product
from forms import SearchForm

# Global variables
# collect all themes
theme_choices = Product.THEME_CHOICES
theme_codes = [theme[0] for theme in theme_choices]
theme_names = [theme[1] for theme in theme_choices]



# HOME views
def index(request):
    import random

    if request.user.is_authenticated:        
        fname = f"{request.session.get('first_name')}".capitalize() 
        lname = f"{request.session.get('last_name')}".capitalize()
        
        # collect themes
        # theme_choices = Product.THEME_CHOICES
        # theme_codes = [theme[0] for theme in theme_choices]
        # theme_names = [theme[1] for theme in theme_choices]

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

        # randomize and pick theme
        rand_theme = random.choice(theme_codes)

        # randomize and pick image
        rand_photo_ind = random.choice(range(photos.count()))
        rand_photo = photos[rand_photo_ind]

        rand_art_ind = random.choice(range(art.count()))
        rand_art = art[rand_art_ind]

        context = {
            "message" : f"{fname} {lname}! Welcome to PG's Picsies!",
            "random_photo" : rand_photo,
            "random_art" : rand_art,
            "theme_label" : theme_label,
            "theme_pictures" : rand_theme_pics,
        }       
        return render(request, 'photostore/index.html', context=context)
    
    else:
        return render(request, 'photostore/index.html')


def search(request):
    

    if request.method == "POST":
        themes = theme_names
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data["query"]
            query_terms = query.split(' ')
            for theme in themes:
                for term in query_terms:
                    if term.lower() == theme.lower(): 
                        search_results = Product.objects.filter(theme=theme)                
                        context = {
                            "query" : query,
                            "search_results" : search_results,
                            }
                        return render(request, 'photostore/search.html', context)
    else:
        form = SearchForm()
        return render(request, 'photostore/search.html', context={"form": form,})




# PRODUCTS views
def products(request):
    all_products = Product.objects.all()

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

    context = {"all_products": content_page,
             }
    return render(request, 'photostore/products.html', context)




# CHECKOUT views
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
