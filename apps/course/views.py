from django.shortcuts import render, redirect
from .models import Course, Description

def index(request):
    context = {
    "courses": Course.objects.all(),
    "desc": Description.objects.all()
    }
    return render(request, "index.html", context)

def process(request):
    cour = Course.objects.create(course = request.POST['course'])
    Description.objects.create(description = request.POST['description'], course_id = cour)
    return redirect('/')

def delete(request, id):
    des = Description.objects.get(id = id)
    context = {
    "name" : des.course_id.course,
    "desc" : des.description,
    "desid": des.id
    }
    return render(request, "del.html", context)

def delprocess(request, id):
    if request.POST['no'] == "No":
        return redirect('/')
    else:
        des = Description.objects.get(id = id)
        des.delete()
        cid = des.course_id.id
        Course.objects.get(id = cid).delete()
        return redirect('/')
