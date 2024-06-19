from django.shortcuts import render

# Create your views here.
def my_first_app(request):
  return render(request, 'myfirstapp/index.html')
