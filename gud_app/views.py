from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from gud_app.models import User
from django.contrib.auth import authenticate, login
import bcrypt

def splash(request):
    return render(request, 'splash.html')

def index(request):
    return render(request, 'index.html')

def men(request):
    return render(request, 'men.html')

def women(request):
    return render(request, 'women.html')

def mission(request):
    return render(request, 'mission.html')

def registration_template(request):
    return render(request,'registration.html')

def registration_user(request):
    errors = User.objects.validate_user(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect('/registration')

    user = User.objects.create_user(
        email=request.POST['email'],
        password=request.POST['password'],
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name']
    )
    messages.success(request, "Successfully registered", extra_tags='register_user')
    return redirect('/registration')

def login_user(request):
    errors = User.objects.validate_login(request.POST)
    if errors:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect("/registration")

    email = request.POST['email_login']
    password = request.POST['password_login']
    user = authenticate(request, username=email, password=password)
    if user is not None:
        login(request, user)
        return redirect('/us')
    else:
        messages.error(request,"Incorrect password", extra_tags='password_not_match')
        # what if user is registered already but typed the wrong password
        return redirect('/registration')

def orders(request):
    return render(request, 'dashboard_orders.html')

def orderDetail(request):
    return render(request, 'dashboard_orders_show.html')

def products(request):
    return render(request, 'dashboard_products.html')

def add(request):
    return render(request, 'dashboard_add_product.html')