from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.splash),
    path('us', views.index),
    path('us/men', views.men),
    path('us/women', views.women),
    path('mission', views.mission),
    path('registration',views.registration_template),
    path('signup', views.registration_user),
    path('login', views.login_user),
    path('logout',views.logout_user),
    path('contact', views.contact),
    path('dashboard/orders', views.orders),
    path('dashboard/orders/show', views.order_detail),
    path('dashboard/products', views.products),
    path('dashboard/products/add', views.add_template),
    path('go_to_add_product',views.go_to_add_product),
    path('add_product', views.add_product),
    path('delete/<int:product_id>',views.delete_product),
    path('addcategory',views.add_categories),
    path('product_detail/<int:product_id>',views.product_detail_template),
    path('edit/<int:product_id>', views.edit_product_template),
    path('update', views.update_product),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)