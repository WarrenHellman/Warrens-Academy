# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    response = "placeholder to later display all the list of blogs"
    return HttpResponse(response)
def new(request):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)
def create(request):
    return redirect('/')
def show(request, num):
    response = 'placeholder to display blog '+str(num)
    return HttpResponse(response)