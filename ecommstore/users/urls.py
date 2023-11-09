from django.urls import path

from . import views
#from users.views import CustomLoginView

# define namespace
app_name = "users"

urlpatterns = [
    # path('login', CustomLoginView.as_view(), name='login'),
    path('login', views.login_view, name='login'),
    path('my_profile', views.user_profile, name='user_profile'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout_view, name='logout'),
    # path('redirect-to-home', views.redirect_to_home, name='redirect_to_home'),
]
