# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import bcrypt

# Create your models here.
# This validates the addition of new users and throws flash messages if the new user info is not in correct format
class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}  
        if len(postData['first'])<3:
            errors['first'] = 'First name must contain at least 3 characters'
        if len(postData['last']) <3:
            errors['last'] = 'Last name must contain at least 3 characters'
        if User.objects.filter(email=postData['email']):
            errors['email'] = 'That email address is already registered'
        if postData['pwd']!= postData['conpwd']:
            errors['password'] = 'Passwords do not match'
        if len(postData['pwd'])<8:
            errors['pwd'] = 'Password must be at least 8 characters'
        return errors
    # A password validator, looks for a matching encrypted password and registered email address
    def logvalidator(self, postData):
        errors = {}
        if not User.objects.filter(email=postData['email']):
            errors['email'] = 'That email address has not been registered'
        user = self.filter(email=postData['email'])

        for word in user:
            if not bcrypt.checkpw(postData['pwd'].encode(), word.password.encode()):
                errors['pwd']='Please check your password'
        
        return errors
        # When updating passwords, this checks for appropriate passwords and whether the password and confirmation match
    def updateValidator(self, postData):
        errors = {}
        if postData['password']!= postData['conpwd']:
            errors['password'] = 'Passwords do not match'
        if len(postData['password'])<8:
            errors['password'] = 'Password must be at least 8 characters'
        
        return errors

# Defines the User class
class User(models.Model):
    first = models.CharField(max_length=100)
    last = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    user_level = models.IntegerField(null=True)
    description = models.CharField(max_length=500)
    # Links our user to the validation functions above
    objects = UserManager()

# Our message class. Poster ID was added to match user names to message for the wall
class Message(models.Model):
    content = models.CharField(max_length=500, null=True, blank=True)
    user = models.ForeignKey(User, related_name='messages')
    poster_id = models.IntegerField(null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
# Our comment class. Poster ID was added to match user names to comments for the wall
class Comment(models.Model):
    content = models.CharField(max_length=500, null=True, blank=True)
    message = models.ForeignKey(Message, related_name='comments')
    poster_id = models.IntegerField(null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)