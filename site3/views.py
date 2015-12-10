from django.shortcuts import render

from . import models

def mainpage(request):
    return render(request, 'mainpage.html')

def material1(request):
    return render(request, 'materials/material1.html')

def material2(request):
    return render(request, 'materials/material2.html')

def material3(request):
    return render(request, 'materials/material3.html')

def materials(request):
    videos = models.YoutubeVideo.objects.all()
    return render(request, 'materials.html', {"videos": videos})

def tasks(request):
    return render(request, 'tasks.html')

def links(request):
    return render(request, 'links.html')