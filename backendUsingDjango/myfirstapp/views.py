from django.shortcuts import render, get_object_or_404
from .models import MyFirstModel

# Create your views here.
def my_first_app(request):
  datas = MyFirstModel.objects.all()
  return render(request, 'myfirstapp/index.html', {'datas': datas})

def my_first_app_detail(request, id):
  data = get_object_or_404(MyFirstModel, pk=id) # pk is the primary key of the data
  return render(request, 'myfirstapp/detail.html', {'data': data})
