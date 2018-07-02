# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt

# Create your views here.
def index(request):
    return render(request, 'dash/index.html')

def signin(request):
    
    return render(request, 'dash/signin.html')

def passcheck(request):
    errors = User.objects.logvalidator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/signin')
    
    else:
        user = User.objects.get(email=request.POST['email'])
        if user.user_level == 9:
            return redirect('/dashboard/admin')
        else: 
            return redirect('/dashboard')

def dashAdmin(request):
    context = {
        'users':User.objects.all()
    }
    return render(request, 'dash/dashAdmin.html', context)

def register(request):
    return render(request, 'dash/register.html')

def dashboard(request):
    context = {
        'users':User.objects.all()
    }
    return render(request, 'dash/dashboard.html', context)

def edit(request, id):
    context= {
        'user': User.objects.get(id=id)
    }    
    return render(request, 'dash/edit.html', context)
def remove(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('/dashboard/admin')

def update(request, id):
    user = User.objects.get(id=id)
    user.email = request.POST['email']
    user.first = request.POST['first']
    user.last = request.POST['last']
    user.save()
    return redirect('/dashboard/admin')

def newUser(request):
    errors = User.objects.validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/register')
    else:
        user = User.objects.create()
        id = user.id
        user.email = request.POST['email']
        user.first = request.POST['first']
        user.last = request.POST['last']
        user.password = request.POST['pwd']
        hashed = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt())
        user.password = hashed
        if user.id == 1:
            user.user_level = 9
        else: 
            user.user_level = 1
        user.save()

        return redirect('/dashboard', {'user':User.objects.get(id=id)})

