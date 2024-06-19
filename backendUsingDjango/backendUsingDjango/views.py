from django.http import HttpResponse

def health(request):
  return HttpResponse("Health is OK!")

def helloworld(request):
  return HttpResponse("Hello World")
