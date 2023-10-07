import datetime

from django import forms
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse


def home(request):
    return render(request, 'home.html', {})

def input_form(request):
    # if this is a POST request we need to process the form data
    form = associates_form()
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        print(request.POST)
    context = {'form':form}
    return render(request, 'associates_form.html', context)
