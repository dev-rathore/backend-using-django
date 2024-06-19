from django.http import HttpResponse
from django.shortcuts import render

def health(request):
  return HttpResponse("Health is OK!")

def helloworld(request):
  return HttpResponse("Hello World")

def templaterender(request):
  return render(request, 'templaterender/index.html')
