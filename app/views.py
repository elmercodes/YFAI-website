from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse

from . forms import CreateUserForm, LoginForm

from django.contrib.auth.models import auth

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from django.core.mail import send_mail


def index(request):
    return render(request, "index.html")

def register(request):
    
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("my-login")
    
    context = {'registerform':form}
    
    return render(request, "register.html", context=context)


def my_login(request):
    
    form = LoginForm
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                auth.login(request, user)
                return redirect("dashboard")
    
    context = {'loginform': form}        
    
    return render(request, "my-login.html", context=context)


@login_required(login_url="my-login")
def dashboard(request):
    return render(request, "dashboard.html")

def privacy_policy(request):
    return render (request, "privacy-policy.html")

def terms_of_use(request):
    return render (request, "terms-of-use.html")

def user_logout(request):
    auth.logout(request)
    return redirect("index")

