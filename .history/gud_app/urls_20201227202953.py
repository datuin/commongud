from django.urls import path
from . import views

urlpatterns = [
    path('', views.splash),
    path('us', views.index),
    path('us/men', views.men),
    path('us/women', views.women),
    path('us/mission', views.mission),
    path('registration',views.registration_template),
    path('signup', views.registration_user),
    path('login', views.login_user)
]
