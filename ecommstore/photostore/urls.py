from django.urls import path

from . import views

#define namespace
app_name = "photostore"

urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search, name='search'),
    path('products', views.products, name='products'),
    path('filter_products', views.filter_products, name='filter_products'),
    path('add-to-cart/<int:product_id>', views.add_to_cart, name='add-to-cart'),    
    path('checkout', views.checkout, name='checkout'),
    path('payment/<str:choice>', views.payment, name='payment'),
    path('about_us', views.about_us, name='about_us'),
    path('license', views.license, name='license'),
]
