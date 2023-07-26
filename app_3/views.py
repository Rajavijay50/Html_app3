from django.shortcuts import render
from django.http import HttpResponse

def string(request):
    return HttpResponse('This is last one of this project')


# Create your views here.
def page1(request):
    return render(request,'page1.html')
def page2(request):
    return render(request,'page2.html')
