from django.shortcuts import render, redirect, HttpResponse
from .models import People
from django.contrib import messages

def index(request):
    return render(request, "users/index.html")

def process(request):
    uname = request.POST['username']
    context = {
    "uname" : uname
    }
    error = People.objects.validate(context)
    if error:
        messages.add_message(request, messages.ERROR, error[0])
        return redirect('/')
    else:
        People.objects.create(username = uname)
        return redirect('/success')

def success(request):
    people = People.objects.all()
    context = {
    "people" : people
    }
    return render(request, "users/success.html", context)
