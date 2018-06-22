# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from time import localtime, strftime
# Create your views here.
def load(request):
    
    if not 'context' in request.session:
        request.session['context']=[]
    
    return render(request, 'session_words/index.html')

def process(request):
    # a work around hack to get a true or false response. Unchecked is false, checked is true
    boolFonts = request.POST['fonts']
    if request.POST['fonts'] == True:
        boolFonts = True
    # handles the checkbox input and changes the font size based on the request
    if boolFonts=='false':
        fonts='15px'
    if boolFonts=='true':
        fonts='40px'
    # a dictionary for storing each word entry in an object
    newContext = {
        'add_word': request.POST['add_word'],
        'color': request.POST['color'],
        'time' : strftime("%Y-%m-%d %H:%M %p", localtime()),
        'fonts': fonts
    }
    tempArray = request.session['context']
    # for some reason we couldn't directly append to request.session[context] but could make a proxy temp array to perform the appending and set them equal to one another
    tempArray.append(newContext)
    request.session['context'] = tempArray

    return redirect( '/session_words/results')

def results(request):
    return redirect('/session_words')

def clear(request):
    del request.session['context']
    return redirect('/session_words')
