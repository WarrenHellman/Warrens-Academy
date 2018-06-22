# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def home(request):
	response = 'Please visit /blogs for blogs, /surveys for surveys and /users for users'
	return HttpResponse(response)

def index(request):
    response = "placeholder to later display all the list of blogs"
    return HttpResponse(response)
def new(request):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)
def create(request):
	if request.method == "POST":
		print "*"*50
		print request.POST
		print request.POST['name']
		print request.POST['desc']
		request.session['name'] = "test"  # more on session below
		print "*"*50
		return redirect("/")
	else:
		return redirect("/")
def show(request, num):
    response = 'placeholder to display blog '+str(num)
    return HttpResponse(response)
def edit(request, num):
    response = 'placeholder to edit blog ' + str(num)
    return HttpResponse(response)
def destroy(request, num):
    return redirect('/')