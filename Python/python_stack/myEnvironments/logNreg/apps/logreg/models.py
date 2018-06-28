# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}  
        if len(postData['first'])<3:
            errors['first'] = 'First name must contain at least 3 characters'
        if len(postData['last']) <3:
            errors['last'] = 'Last name must contain at least 3 characters'
        if User.objects.filter(email=postData['email']):
            errors['email'] = 'That email address is already registered'
        if postData['password']!= postData['confirm']:
            errors['password'] = 'Passwords do not match'
        if len(postData['password'])<8:
            errors['password'] = 'Password must be at least 8 characters'
        return errors
        
    def logvalidator(self, postData):
        errors = {}
        if not User.objects.filter(email=postData['log-email']):
            errors['log-email'] = 'That email address has not been registered'
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    # doesn't account for unqiue values
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)

    objects = UserManager()