from django.urls import path
from . import views

urlpatterns = [
    path('', views.splash),
    path('us', views.index),
    path('us/men', views.men),
    path('us/women', views.women),
    path('mission', views.mission),
    path('registration',views.registration_template),
    path('signup', views.registration_user),
    path('login', views.login_user),
    path('contact', views.contact),
    path('dashboard/orders', views.orders),
    path('dashboard/orders/show', views.orderDetail),
    path('dashboard/products', views.products),
    path('dashboard/products/add', views.add),
]
