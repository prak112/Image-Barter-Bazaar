from django.urls import path

from . import views

#define namespace
app_name = "photostore"

urlpatterns = [
    path('', views.index, name='index'),
    path('products', views.products, name='products'),
    path('checkout', views.checkout, name='checkout'),
    path('about_us', views.about_us, name='about_us'),
]
