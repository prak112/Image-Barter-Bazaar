from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView, LogoutView

from users.forms import LoginForm, RegForm

# Views
# REGISTRATION
def signup(request):
    # import UserProfile, password hashing lib
    from users.models import UserProfile
    from django.contrib.auth.hashers import make_password
    
    # validate request
    if request.method == "POST":
        form = RegForm(request.POST)

        if form.is_valid():
            # capitalize name
            
            # hash user-provided password
            raw_password = form.cleaned_data["password"]
            hashed_password = make_password(raw_password)
            user = UserProfile(password=hashed_password)
            user.save()
            # form.cleaned_data["password"]
            # form.save() 

            name = f"{form.cleaned_data['first_name']} {form.cleaned_data['last_name']}"
            context={"message": f"Account created. Welcome, {name.capitalize()}, to PG's Picsies!"}
            return render(request, 'photostore/index.html', context=context)
        else:
            return render(request, 'users/signup.html', context={"form": form})

    else:
        return render(request, 'users/signup.html', context={"form": RegForm()})



# LOGIN
class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    authentication_form = LoginForm
    # to check def get_success_url
    success_url = 'index'



def user_profile(request):
    return render(request, 'users/user_profile.html')



# LOGOUT
def logout_view(request):
    logout(request)
    request.session.clear()

    return render(request, 'users/login.html',context={
          "message" : "Logged out successfully! Missed something ?"
    })
    

def redirect_to_home(request):
        return redirect(reverse('photostore:index'))