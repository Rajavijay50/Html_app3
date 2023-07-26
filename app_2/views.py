from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def string(request):
    return HttpResponse('<h1>This is string response</h1>')
def home1(request):
    return render(request,'home1.html')
def home2(request):
    return render(request,'home2.html')