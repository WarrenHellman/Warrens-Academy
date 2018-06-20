# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.crypto import get_random_string
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    # defines a variable word to a new random string each time
    word = get_random_string(length=14)
    # defines a variable count that starts at 1
    count = request.session.get('count', 1)
    # each reset through the generate button or refresh adds onto count variable
    request.session['count']=count+1
    # context object returns the new word and the current session of count
    context = {
        'random' : word,
        'attempt': request.session['count']
    }
    # shows the template to show, our request and context values
    return render(request, "random_string/index.html", context)

def generate(request):
    
    if request.method == 'POST':
        
        return redirect('/generate')
    else:
        return redirect('/')
def reset(request):
    if request.method == 'POST':
        request.session['count']=0
        return redirect('/reset')
    else:
        return redirect ('/')