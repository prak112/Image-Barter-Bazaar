from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView, LogoutView

from users.forms import RegForm

# Views
# REGISTRATION
def signup(request):
    # import UserProfile model
    from users.models import UserProfile
    
    # validate request
    if request.method == "POST":
        form = RegForm(request.POST)

        if form.is_valid():
            # process user data using Django ORM commands
            # password = request.user.set_password(request.user.password)
            user = UserProfile(
                first_name=request.user.first_name,
                last_name=request.user.last_name,
                email=request.user.email,
                username=request.user.username,
                password=request.user.password,
                customer_type=request.user.customer_type,
                bio=request.user.bio
                  )
            
            # save form, authenticate user
            user = form.save()
            login(request, user)

            # create user session data
            request.session['first_name'] = user.first_name
            request.session['last_name'] = user.last_name

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

            # create user session data
            request.session['first_name'] = user.first_name
            request.session['last_name'] = user.last_name

            return HttpResponseRedirect(reverse('photostore:index'))
    
    else: 
        return render(request, 'users/login.html', context={"form": AuthenticationForm()})



# class CustomLoginView(LoginView):
#     template_name = 'users/login.html'
#     authentication_form = LoginForm

#     def get_success_url(self) -> str:
#         # create user session data
#         self.session['first_name'] = self.first_name
#         self.session['last_name'] = self.last_name

#         return reverse('photostore:index')


def user_profile(request):
    return render(request, 'users/user_profile.html')



# LOGOUT
def logout_view(request):
    logout(request)
    request.session.clear()

    return render(request, 'users/login.html',context={
          "message" : "Logged out successfully! Missed something ?"
    })
    

# unknown usage
# def redirect_to_home(request): 
#         return redirect(reverse('photostore:index'))