from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from gud_app.models import User, Category, Product , Image
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

def splash(request):
    return render(request, 'splash.html')

def index(request):
    return render(request, 'index.html')

def men(request):
    all_products = Product.objects.all()
    print("heeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeereeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeetoooo")
    print(all_products.first().images.first().image.url)
    context= {
        'products': all_products
    }
    return render(request, 'men.html', context)

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
        page = request.POST['url']
        return redirect(page)
    else:
        messages.error(request,"Incorrect password", extra_tags='password_not_match')
        # what if user is registered already but typed the wrong password
        return redirect('/registration')

def logout_user(request):
    logout(request)
    return redirect("/us")

def order_detail(request):
    return render(request, 'dashboard_orders_show.html')

def products(request):
    all_products = Product.objects.all()
    all_images = Image.objects.filter(name="image_1")
    context= {
        'products': all_products,
        'images': all_images
    }
    return render(request, 'dashboard_products.html',context)

def add_template(request):
    all_categories = Category.objects.all()

    context ={
        'categories': all_categories
    }
    return render(request, 'dashboard_add_product.html',context)

def orders(request):
    return render(request, 'dashboard_orders.html')

def go_to_add_product(request):
    return redirect("/dashboard/products/add")

def add_product(request):
    errors = User.objects.validate_product(request.POST)

    if errors:
        for key,value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect("/dashboard/products/add")

    print("heeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeereeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
    print(request.FILES['image_1'].name)
    product = Product.objects.create(
        name=request.POST['name'],
        description=request.POST['description'],
        price=request.POST['price'],
        product_category=Category.objects.get(id=request.POST['category']),
        user=request.user,
        size=request.POST['size'],
        color=request.POST['color'],
        gender=request.POST['gender']
    )
    Image.objects.create(name="image_1", product=product, image=request.FILES['image_1'])
    Image.objects.create(name="image_2", product=product, image=request.FILES['image_1'])
    Image.objects.create(name="image_3", product=product, image=request.FILES['image_1'])
    return redirect("/dashboard/products")

def delete_product(request,product_id):
    product = Product.objects.get(id= product_id)
    product.delete()
    messages.success(request,"You delete this product", extra_tags='product_deleted')
    return redirect("/dashboard/products")

