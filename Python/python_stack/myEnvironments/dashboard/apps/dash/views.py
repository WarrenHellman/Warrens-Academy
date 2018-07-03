# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import User, Message
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
def updatepwd(request, id):
    user = User.objects.get(id=id)
    errors = User.objects.updateValidator(request.POST)
    if len(errors):
        id=user.id
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/users/edit/'+str(id))
    
    else:
        user = User.objects.get(id=id)
        user.password = request.POST['password']
        hashed = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt())
        user.password = hashed
        user.save()
        return redirect('/dashboard/admin')

def update(request, id):
    user = User.objects.get(id=id)
    user.email = request.POST['email']
    user.first = request.POST['first']
    user.last = request.POST['last']
    if request.POST['user_level']=='Admin':
        user.user_level=9
    else:
        user.user_level=1
    user.save()
    return redirect('/dashboard/admin')
def add(request):
    return render(request, 'dash/add.html')

def addUser(request):
    # Could make this DRY by making the error section and create user section their own functions
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
        user.user_level = 1
        user.save()

        return redirect('/dashboard/admin', {'user':User.objects.get(id=id)})
    
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

def editUser(request, id):
    context = {
        'user' : User.objects.get(id=id)    
    }
    return render(request, ('dash/userEdit.html'), context)
def description(request, id):
    user=User.objects.get(id=id)
    user.description = request.POST['description']
    user.save()
    return redirect('/dashboard')
def userpage(request, id):
    context = {
        'user' : User.objects.get(id=id)    
    }
    return render(request, ('dash/userpage.html'), context)
def postmsg(request, id):
    user = User.objects.get(id=id)
    id= user.id
    context = {
        'user' : User.objects.get(id=id)    
    }
    message = Message.objects.create()
    message.content = request.POST['leavemsg']
    message.save()

    return redirect('/users/show'+str(id), context)