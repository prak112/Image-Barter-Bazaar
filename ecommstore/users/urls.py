from django.urls import path

from . import views

# define namespace
app_name = "users"

urlpatterns = [
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout, name='logout'),
    path('redirect-to-home', views.redirect_to_home, name='redirect_to_home'),
]
