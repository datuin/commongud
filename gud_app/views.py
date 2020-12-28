from django.shortcuts import render, HttpResponse

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

def contact(request):
    return render(request, 'contact_us.html')