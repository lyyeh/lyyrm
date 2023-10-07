from datetime import datetime

from django import forms
from django.shortcuts import render, get_object_or_404 , redirect
from django.http import HttpResponse , HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from .models import associate

from .associate_forms import associate_form,associate_detail


def thank_you(request):
    return render(request, 'home.html', {})

def associate_list(request):
    associate_list = associate.objects.all()
    return render (request, 'associates_list.html' , {'associate_list': associate_list})

def associate_record(request, associate_id):
    associate_record = associate.objects.get(pk=associate_id)
    return render (request, 'associates_record.html' , {'associate_record': associate_record})

def associate_update(request, associate_id):
    associate_record = associate.objects.get(pk=associate_id)
    form = associate_detail(request.POST or None, instance=associate_record)
    if form.is_valid():
        form.save()
        return redirect('associate_record')
    
    return render (request, 'associates_update.html' , {'associate_record': associate_record , 'form':form})
    
def associate_search(request):
    #queried = False
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        queried = request.POST['queried']
        record_search = associate.objects.filter(contactemail__contains=queried)
        #form = search_form(request.POST)
        #if form.is_valid()

        return render (request, 'associates_search.html' , {'queried': queried,'record_search':record_search})
    else:
    
        return render (request, 'associates_search.html' , {})

def associate_add(request):
    submitted = False
    
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
    # create a form instance and populate it with data from the request:
        form = associate_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add?submitted=True')
    else:
        form = associate_form
        if 'submitted' in request.GET:
            submitted = True
    
    return render(request, 'associates_add.html', {'form':form, 'submitted':submitted})

class recordlist(ListView):
    model = associate
    template_name = 'associates_list.html'

class recorddetail(DetailView):
    model = associate
    template_name = 'associates_detail.html'

class addrecord(CreateView):
    model = associate
    form_class = associate_form
    template_name = 'associates_add.html'

    

