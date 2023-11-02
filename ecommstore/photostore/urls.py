from django.urls import path

from . import views

#define namespace
app_name = "photostore"

urlpatterns = [
    path('', views.index, name='index'),
    path('products', views.products, name='products'),
#    path('search/<str:query>', views.search, name='search'),
    path('checkout', views.checkout, name='checkout'),
    path('about_us', views.about_us, name='about_us'),
    path('license', views.license, name='license'),
]
