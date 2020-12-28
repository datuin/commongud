from django.db import models
from django.contrib.auth.models import AbstractUser
import re

# Create your models here.

#Tables // User, Products, Categories, wishlist
# User - Products 1- to many
# Products - Category 1 to many
# Wishlist - Products 1 to many

class UserManager(models.Manager):

    def _is_email_valid(email):
        regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        return regex.match().match(email)

    def validate_user(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = 'first name must be at least 2 characters.'
        if len(postData['last_name']) < 2:
            errors['last_name'] = 'last name must be at least 2 characters.'

        elif User.objects.filter(email=postData['email']).exists()
            errors['email_exist'] = 'Invalid email address. email has already been used.'
        if len(postData['password']) < 8:
            errors['password'] = 'Password must be at least 8 characters'
        if postData['password'] != postData ['confirm_pass']:
            errors["confirm_pass"] = "Password confirm does not match"
        return errors

    def validate_login(self, postData):
        errors = {}
        # validating email
        if not UserManager._is_email_valid(postData['email']):
            errors['email'] = "Invalid email address"
        #if email exist
        if not User.objects.filter(email = postData['email_login']).exists():
            errors['email_notexist']= "This email does not exist"
        return errors

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

class Product(models.Model):
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=45)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(default=None)
    product_category = models.ForeignKey(Category,related_name="products", on_delete= models.CASCADE)
    user = models.ForeignKey(User, related_name="products_from_user", on_delete= models.CASCADE)
    size = models.CharField(max_length=45)
    color = models.CharField(max_length=45)
    gender = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Wishlist(models.Model):
    wish_product = models.ForeignKey(Product, related_name="wishlist", on_delete = models.CASCADE)
    quantity = models.IntegerField()
