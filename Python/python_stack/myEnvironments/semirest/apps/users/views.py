# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse
from .models import User
# Create your views here.
def index(request):
    # Need to include the dictionary so that we can autopopulate the users table
    return render(request, 'users/index.html', {'users' : User.objects.all()})

def new(request):
    return render(request, 'users/new.html')

def create(request):
    errors = User.objects.validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/users/create')
    else:

        user = User.objects.create()
        id = user.id
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
        return redirect('/users/'+str(id), {'user': User.objects.get(id=id)})

def show(request, id):
    # Need to pass either a context dictionary (more useful with lots of data) or just a single value like we did above
    # context = {
    #     'user':User.objects.get(id=id)
    # }
    
    return render(request, 'users/show.html', {'user': User.objects.get(id=id)} )

def destroy(request, id):
    context = {
        'user':User.objects.get(id=id)
    }
    b = User.objects.get(id=id)
    b.delete()
    return redirect('/users', context)

def update(request, id):
    
    user = User.objects.get(id=id)
    id = user.id
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.email = request.POST['email']
    user.save()
    return redirect('/users/'+str(id))

def edit(request, id):
    context = {
        'user':User.objects.get(id=id)
    }
    return render(request, 'users/edit.html', context)