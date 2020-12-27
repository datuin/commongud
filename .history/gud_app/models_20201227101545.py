from django.db import models
import re

# Create your models here.

#Tables // User, Products, Categories, wishlist
# User - Products 1- to many
# Products - Category 1 to many
# Wishlist - Products 1 to many

class UserManager(models.Manager):
    def validateUser(self, postData):
        errors = {}

        if len(postData['first']) == 0:
            errors['first'] = 'First Name is required'
        elif len(postData['first']) < 2:
            errors['first'] = 'First Name must be at least 2 characters.'
        if len(postData['last']) == 0:
            errors['last'] = 'Last Name is required'
        elif len(postData['last']) < 2:
            errors['last'] = 'Last Name must be at least 2 characters.'
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address"
        email_Exists = User.objects.filter(email=postData['email'])
        if email_Exists:
            errors['email_Exists'] = 'Invalid email address. Email has already been used. '
        if len(postData['password']) < 8:
            errors['password'] = 'Password must be at least 8 characters'
        if len(postData['password']) != len(postData['confirm_password']):
            errors['confirm_password'] = 'Password does not match'
        return errors

    def validateLogin(self, postData):
        errors = {}

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['theEmail'] = "Invalid email address"
        email_Exists = User.objects.filter(email=postData['email'])
        if not email_Exists:
            errors['theEmail'] = 'Email does not exist'
        if len(postData['password']) < 8:
            errors['thePassword'] = 'Incorrect password.'
        return errors

class User(models.Model):
    first = models.CharField(max_length=25)
    last = models.CharField(max_length=25)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

# class Products(models.Model):
#     name = modes.CharField(max_length=45)
    