from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def string(request):
    return HttpResponse('<h1>This is string program work</h1>')
def work1(request):
    return render(request,'work1.html')
def work2(request):
    return render(request,'work2.html')