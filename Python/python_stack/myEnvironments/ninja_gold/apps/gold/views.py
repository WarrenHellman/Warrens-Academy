# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from random import randint
from django.shortcuts import render, redirect
from time import strftime, localtime
# Create your views here.
def index(request):
    # creates the context array and gold amount if not already created
    if not 'context' in request.session: 
        request.session['context']=[]
    if not 'gold' in request.session: 
        request.session['gold']=0
    return render(request, 'gold/index.html')

def process(request):
    # handles the incoming information through the hidden input and separates out the logic
    building = request.POST['building']
    if building == 'farm':
        amount = randint(10,20)
        request.session['gold']+=amount
    elif building == 'cave':
        amount = randint(5,10)
        request.session['gold']+= amount
    elif building == 'house':
        amount = randint(2,5)
        request.session['gold']+=amount
    else:
        amount = randint(-50,50)
        request.session['gold']+=amount

    # creates a new context object, Each object is appended to the context array
    newContext = {
        'amount': amount,
        'time' : strftime("%Y-%m-%d %H:%M %p", localtime()),
        'building': building
    }
    tempArray = request.session['context']
    # for some reason we couldn't directly append to request.session[context] but could make a proxy temp array to perform the appending and set them equal to one another
    tempArray.append(newContext)
    request.session['context'] = tempArray

    return redirect('/')

def clear(request):
    # clears our cookies
    request.session['gold']=0
    request.session['context'] = []
    return redirect('/')