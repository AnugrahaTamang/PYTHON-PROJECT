from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("I am from Home bar")
    return render(request, 'website/index.html')

def contact(request):
    return HttpResponse("I am from contact page")

def about(request):
    return HttpResponse("I am from About page")
