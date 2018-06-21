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
    if boolFonts=='false':
        fonts='15px'
    if boolFonts=='true':
        fonts='40px'
    newContext = {
        'add_word': request.POST['add_word'],
        'color': request.POST['color'],
        'time' : strftime("%Y-%m-%d %H:%M %p", localtime()),
        'fonts': fonts
    }
    tempArray = request.session['context']

    tempArray.append(newContext)
    request.session['context'] = tempArray



    return redirect( '/session_words/results')

def results(request):
    return redirect('/session_words')

def clear(request):
    del request.session['context']
    return redirect('/session_words')
