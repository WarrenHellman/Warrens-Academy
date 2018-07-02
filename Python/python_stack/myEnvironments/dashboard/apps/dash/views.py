# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'dash/index.html')

def signin(request):
    return render(request, 'dash/signin.html')

def register(request):
    return render(request, 'dash/register.html')

def dashboard(request):
    return render(request, 'dash/dashboard.html')

def newUser(request):
    # Add flash messages
    user = User.objects.create()
    id = user.id
    user.first = request.POST['first']
    user.last = request.POST['last']
    user.email = request.POST['email']
    user.password = request.POST['pwd']
    
    user.save()

    return redirect('/', {'user':User.objects.get(id=id)})

