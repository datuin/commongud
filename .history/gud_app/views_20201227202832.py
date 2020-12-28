from django.shortcuts import render, HttpResponse,redirect
from django.contrib import messages
from gud_app.models import User
from django.contrib.auth import authenticate
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
    errors = User.objects.validateUser(request.POST)

    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect('/registration')
    else:
        first = request.POST['first_name']
        last = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        User.objects.create(first=first,last=last,email=email, password=pw_hash)
        messages.success(request, "successfully registered", extra_tags='register_user')
    return redirect('/registration')

def login_user(request):
    errors = User.objects.validateLogin(request.POST)

    if errors:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect("/registration")
    else:
        user = User.objects.filter(email=request.POST['email_login'])
        if user:
            logged_user = user[0]
            if bcrypt.checkpw(request.POST['password_login'].encode(), logged_user.password.encode()):
            request.session['userid'] = logged_user.id
            return redirect('/us')
        messages.error(request,"Incorrect Password", extra_tags='password_not_match')
    return redirect('/us')