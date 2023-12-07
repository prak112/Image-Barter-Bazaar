from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect

from django.contrib.auth import login, logout
# from django.contrib.auth.views import LoginView, LogoutView   # in urls.py, for django-automated templates and validation

from users.forms import RegForm
from users.models import UserProfile


# Views
# REGISTRATION
def signup(request):    
    # validate request
    if request.method == "POST":
        form = RegForm(request.POST)

        if form.is_valid():          
            # save form, authenticate user
            user = form.save()
            login(request, user)

            # user session data identifier
            session_user = UserProfile.objects.get(first_name=user.first_name)
            request.session['user_id'] = session_user.id
            # session variables
            request.session['first_name'] = str(user.first_name).capitalize()
            request.session['last_name'] = str(user.last_name).capitalize()
            request.session.save()

            return HttpResponseRedirect(reverse('photostore:index'))
        
        else: # errors in registration details
            return render(request, 'users/signup.html', context={"form": form})
    else: # GET request response
        return render(request, 'users/signup.html', context={"form": RegForm()})



# LOGIN
def login_view(request):
    from django.contrib.auth.forms import AuthenticationForm

    # validate and authenticate user
    if request.method=="POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            # user session data identifier
            session_user = UserProfile.objects.get(first_name=user.first_name)
            request.session['user_id'] = session_user.id

            # session variables
            request.session['first_name'] = str(user.first_name).capitalize()
            request.session['last_name'] = str(user.last_name).capitalize()
            request.session.save()

            return HttpResponseRedirect(reverse('photostore:index'))    
    else: 
        return render(request, 'users/login.html', context={"form": AuthenticationForm()})
    


def user_profile(request):
    return render(request, 'users/user_profile.html')
# def edit_profile(request):
#     return render(request, 'users/edit_profile.html')



# LOGOUT
def logout_view(request):
    logout(request)
    request.session.clear()

    return render(request, 'users/logout.html',context={
          "message" : "Logged out successfully!"
    })
    
