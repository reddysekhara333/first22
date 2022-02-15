from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def hello(request):
    return render(request,'myapp/base.html')
def welcome(request):
    return render(request,'myapp/home.html')
def course(request):
    return render(request,'myapp/course.html')