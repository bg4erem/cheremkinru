from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'mainpage/home.html')

def projects(request):
    return render(request, 'mainpage/projects.html')

def resume(request):
    return render(request, 'mainpage/resume.html')

def contacts(request):
    return render(request, 'mainpage/contacts.html')