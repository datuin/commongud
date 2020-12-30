from django.db import models
from django.contrib.auth.models import (AbstractUser, BaseUserManager)
import re

# Create your models here.

#Tables // User, Products, Categories, wishlist, orders, billing
# User - Products 1- to many
# Products - Category 1 to many
# Wishlist - Products 1 to many
# orders from user 1 yo many from products many to many
# billing addres from user 1 to many

class UserManager(BaseUserManager):

    def _is_email_valid(email):
        regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        return regex.match(email)

    def validate_user(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = 'first name must be at least 2 characters.'
        if len(postData['last_name']) < 2:
            errors['last_name'] = 'last name must be at least 2 characters.'
        if not UserManager._is_email_valid(postData['email']):
            errors['email'] = "Invalid email address"
        elif User.objects.filter(email=postData['email']).exists():
            errors['email_exist'] = 'Invalid email address. email has already been used.'
        if len(postData['password']) < 8:
            errors['password'] = 'Password must be at least 8 characters'
        if postData['password'] != postData['confirm_pass']:
            errors["confirm_pass"] = "Password confirm does not match"
        return errors

    def validate_login(self, postData):
        errors = {}
        # validating email
        if not UserManager._is_email_valid(postData['email_login']):
            errors['email'] = "Invalid email address"
        #if email exist
        if not User.objects.filter(email = postData['email_login']).exists():
            errors['email_notexist']= "This email does not exist"
        return errors

    def validate_product(self, postData):
        errors = {}
        if len(postData['name']) < 2:
            errors['name'] = "Please insert a valid name"
        if len(postData['description']) < 10:
            errors['description'] = "Please be more specific"
        if len(postData['price']) < 2:
            errors['price'] = "Please insert a valid price"
        if len(postData['size']) < 0:
            errors['size'] = "Please select a size"
        if len(postData['color']) < 2:
            errors['color'] = "Please insert a valid color"
        if len(postData['gender']) < 0:
            errors['gender'] = "Please select a gender"
        if len(postData['category']) < 0:
            errors['category'] = "Please select a category"
        return errors

    def create_user(self, email, password, first_name, last_name):
        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email = self.normalize_email(email),
            password=password,
            first_name = 'Admin',
            last_name = 'name'
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractUser):
    # first_name - first
    # last_name - last
    # email
    # password
    # date_joined - created_at
    # updated_at, why do we need this field?
    username = None
    email = models.EmailField(max_length=45, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

class Category(models.Model):
    name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user_order = models.ForeignKey(User, related_name="orders_from_user", on_delete= models.CASCADE)
    quantity =models.IntegerField()
    total =  models.CharField(max_length=45)
    size = models.CharField(max_length=45)
    #products = all products from this order

class Product(models.Model):
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=45)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    product_category = models.ForeignKey(Category,related_name="products", on_delete= models.CASCADE)
    user = models.ForeignKey(User, related_name="products_from_user", on_delete= models.CASCADE)
    product_order = models.ManyToManyField(Order, related_name="products_order")
    size = models.CharField(max_length=45)
    color = models.CharField(max_length=45)
    gender = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class OrderItem(models.Model):
    product = models.ForeignKey(Product, related_name="order_items", on_delete= models.CASCADE)
    quantity = models.IntegerField()
    price = price = models.DecimalField(max_digits=5, decimal_places=2)
    size = models.CharField(max_length=45)

class Wishlist(models.Model):
    wish_product = models.ForeignKey(Product, related_name="wishlist", on_delete = models.CASCADE)
    quantity = models.IntegerField()

class Image(models.Model):
    name = models.CharField(max_length=255)
    product = models.ForeignKey(Product, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    default = models.BooleanField(default=False)