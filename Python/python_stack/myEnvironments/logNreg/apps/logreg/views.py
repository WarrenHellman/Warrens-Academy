# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import User
from django.shortcuts import render, redirect
from django.contrib import messages
# can't import bcrypt but this runs if you run the server from the command line, uncomment import and register function call
# import bcrypt


# Create your views here.
def index(request):

    return render(request, 'logreg/index.html')


def register(request):
    errors = User.objects.validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:

        user = User.objects.create()
        id = user.id
        user.first_name = request.POST['first']
        user.last_name = request.POST['last']
        user.email = request.POST['email']
        user.password = request.POST['password']

        # uncomment
        # hashed = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt())
        # user.password = hashed

        user.save()
        request.session['method']='registered'
        return redirect('/success/register/'+str(id), {'user':User.objects.get(id=id)})

def success(request, id):
    return render(request, 'logreg/success.html', {'user':User.objects.get(id=id)})

def login(request):
    errors = User.objects.logvalidator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        email = request.POST['log-email']
        # if User.objects.get(email=email):
        request.session['method']='logged in'
        user = User.objects.get(email=email)
        id = user.id
        return redirect('/success/login/'+str(id), {'user':User.objects.get(id=id)})
    # else: 
    #     print 'nope'
    #     return redirect('/')