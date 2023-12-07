# import libraries
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

# app-related imports
from photostore.models import Product, Cart, Order#, OrderDetail
from users.models import UserProfile
from photostore.forms import SearchForm, PaymentForm
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
    item_to_add = Product.objects.get(id=product_id)   

    # if user authenticated, insert data to Cart model
    if request.user.is_authenticated:
        #user_id = request.session.get('user_id')
        user_info = UserProfile.objects.get(first_name=request.user.first_name)
        cart_item = Cart()
        cart_item.customer_info = user_info
        cart_item.item = item_to_add

        # retrieve quantity
        cart_item.quantity = request.POST.get('quantity')
        if cart_item.quantity is None:
            cart_item.quantity = 1 # default value
                  
        # save cart info
        cart_item.save()

        # redirect to calling view
        calling_url = request.META.get('HTTP_REFERER')

        #TO DO - show notification
        return redirect(calling_url)
    else:
        return HttpResponseRedirect(reverse('users:login'))

    # context = {
    #     'cart' : Cart.objects.all(),
    #     }
    # return render(request, 'photostore/checkout.html', context)


def remove_from_cart(request, product_id):
    if request.user.is_authenticated:
        cart_item = Cart.objects.get(id=product_id)
        cart_item.delete()
        
        # get referrer URL or calling_url
        calling_url = request.META.get('HTTP_REFERER')
    return redirect(calling_url)


def checkout(request):
    if request.user.is_authenticated:
        # if user made payment, clear cart_info
        cart_info = Cart.objects.filter(customer_info=UserProfile.objects.get(first_name=request.user.first_name))

        context = {
            'cart' : cart_info,
            }
        return render(request, 'photostore/checkout.html', context)
    else:
        return HttpResponseRedirect(reverse('users:login'))
        # after login, revert back to redirect view



def payment(request):
    # retrieve all 'Cart' instances (items in cart) of user logged in for context
    cart_info = Cart.objects.filter(customer_info__first_name=request.user.first_name)
    # order 'Cart' instances by id for 'Order.customer_order'
    cart_sorted = cart_info.order_by('-id').first()

    if request.method == 'POST':
        form = PaymentForm(request.POST, request.FILES)   # request.FILES to access uploaded image

        if form.is_valid():
            # save 'Product' instance from PaymentForm
            payment_info = form.save(commit=False)
            payment_info.save()

            # insert data sequentially for 'Order' model
            purchase_order = Order()            
            purchase_order.customer_order = cart_sorted

            if form.cleaned_data['delivery'] == 'EMAIL':
                purchase_order.order_status = 'DEL'
            else:
                purchase_order.order_status = 'SHIP'
            
            purchase_order.payment = payment_info
            purchase_order.save()

            context = {
                'message' : 'Thanks for shopping with us! See you soon!'    
                }
            
            return render(request, 'photostore/index.html', context)
            #return HttpResponseRedirect(reverse('photostore:index'))
        
        else:   # validate incomplete form
            context = {
                'cart' : cart_info,
                'form' : form,
                }
            return render(request, 'photostore/payment.html', context)
    
    else:   # first visit to payment
        context = {
            'cart' : cart_info,
            'form' : PaymentForm(),
            }
        return render(request, 'photostore/payment.html', context)



# OTHER views
def about_us(request):
    return render(request, 'photostore/about_us.html')

def license(request):
    return render(request, 'photostore/license.html')
