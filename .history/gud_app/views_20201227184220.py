from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from gud_app.models import User
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
    return redirect('/registration')
    # else:
    #     first = request.POST['first_name']
    #     last = request.POST['last_name']
    #     email = request.POST['email']
    #     password = request.POST['password']
    #     pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    #     User.objects.create_user(first_name=first,last_name=last,email=email, password=pw_hash)
    #     messages.success(request, "successfully registered", extra_tags='register_user')
    #     return redirect('/registration')
