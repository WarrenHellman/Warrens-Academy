# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
# loads the index page
def index(request):
    return render(request, "form/index.html")
# stores the form values in session so the can be called later in our results page. I don't know why I say our
def process(request):
    request.session['city']=request.POST['city']
    request.session['name']=request.POST['name']
    request.session['language']=request.POST['language']
    request.session['comments']=request.POST['comments']
    count=request.session.get('count',1)
    request.session['count']=count+1
    # just processes here and redirects to our results for results page rendering
    return redirect('/results')

def results(request):
    return render(request, 'form/results.html')