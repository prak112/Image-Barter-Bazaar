from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect


from django.contrib.auth import authenticate, login, logout

# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username, password)
        
        if user:
            login(request, user)
            request.session["username"] = user.username
            return HttpResponseRedirect(reverse('photostore:index'))
        
        else:
            return render(request, 'users/login.html', context={
          "message" : "Invalid Credentials! Are you sure you did not miss anything ?"
          })

    else:
        return render(request, 'users/login.html')

def signup(request):
    return render(request, 'users/signup.html')


def logout(request):
    logout(request)

    return render(request, 'users/login.html',context={
          "message" : "Logged out successfully! Missed something ?"
    })
    

def redirect_to_home(request):
        return redirect(reverse('photostore:index'))