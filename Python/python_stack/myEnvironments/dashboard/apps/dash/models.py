# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}  
        # if len(postData['first'])<3:
        #     errors['first'] = 'First name must contain at least 3 characters'
        # if len(postData['last']) <3:
        #     errors['last'] = 'Last name must contain at least 3 characters'
        # if User.objects.filter(email=postData['email']):
        #     errors['email'] = 'That email address is already registered'
        # if postData['password']!= postData['confirm']:
        #     errors['password'] = 'Passwords do not match'
        # if len(postData['password'])<8:
        #     errors['password'] = 'Password must be at least 8 characters'
        return errors
        
    def logvalidator(self, postData):
        errors = {}
        # if not User.objects.filter(email=postData['log-email']):
        #     errors['log-email'] = 'That email address has not been registered'
        # user = self.filter(email=postData['log-email'])

        # uncomment below
        # for word in user:
            # if not bcrypt.checkpw(postData['password'].encode(), word.password.encode()):
            #     errors['password']='Passwords do not match'
        
        return errors


class User(models.Model):
    first = models.CharField(max_length=100)
    last = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    user_level = None
    
    objects = UserManager()