# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    if not request.session.get('shirts'):
        request.session['shirts']=0
    if not request.session.get('hats'):
        request.session['hats']=0
    if not request.session.get('coozies'):
        request.session['coozies']=0
    if not request.session.get('product_id'):
        request.session['product_id']=0
    if not request.session.get('grandTotal'):
        request.session['grandTotal']=0
    return render(request, 'shopping/index.html')

def buy(request):
    if request.POST.get('shirts'):
        request.session['shirts']+=int(request.POST['shirts'])
        itemsOrdered=int(request.POST['shirts'])
    if request.POST.get('hats'):
        request.session['hats']+=int(request.POST['hats'])
        itemsOrdered=int(request.POST['hats'])
    if request.POST.get('coozies'):
        request.session['coozies']+=int(request.POST['coozies'])
        itemsOrdered=int(request.POST['coozies'])
    request.session['product_id']=(request.POST['product_id'])

    prices = {
        '4': 19.99,
        '5': 9.99,
        '6': 4.99,
    }
    
    request.session['total'] = prices[request.session['product_id']]*(itemsOrdered)
    request.session['itemNum']=request.session['shirts']+request.session['hats']+request.session['coozies']
    request.session['grandTotal']+=request.session['total']




    return redirect('/purchase')

def purchase(request):

    return render(request, 'shopping/purchase.html')

def clear(request):

    request.session['shirts'] = 0
    request.session['hats'] = 0
    request.session['coozies'] = 0
    request.session['product_id'] = 0
    request.session['grandTotal'] = 0

    return redirect('/')