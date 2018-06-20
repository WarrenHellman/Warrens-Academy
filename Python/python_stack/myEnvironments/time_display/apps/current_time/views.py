# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime, localtime
# Create your views here.
def index(request):
    # response = "time placeholder"
    context = {
        'time1': strftime("%Y-%m-%d %H:%M %p", gmtime()),
        'time2': strftime("%Y-%m-%d %H:%M %p", localtime())
    }
    return render(request, 'current_time/index.html', context)