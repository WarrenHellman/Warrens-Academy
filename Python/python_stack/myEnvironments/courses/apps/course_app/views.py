# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Course

# Create your views here.
def index(request):
    
    return render(request, 'course_app/index.html', {'courses': Course.objects.all()})

def add(request):
    
    errors = Course.objects.validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        print request.POST['name']
        course = Course.objects.create()
        course.name = request.POST['name']
        id = course.id
        course.description = request.POST['description']
        course.save()

        return redirect('/', {'course': Course.objects.get(id=id)})

def delete(request, id):
    context = {
        'course':Course.objects.get(id=id)
    }
    return render(request, 'course_app/delete.html', context)
def destroy(request, id):
    context = {
        'course':Course.objects.get(id=id)
    }
    course = Course.objects.get(id=id)
    course.delete()
    return redirect ('/', context)