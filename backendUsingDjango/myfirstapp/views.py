from django.shortcuts import render, get_object_or_404
from .models import MyFirstModel, Tag
from .forms import ReviewForm

# Create your views here.
def my_first_app(request):
  datas = MyFirstModel.objects.all()
  return render(request, 'myfirstapp/index.html', {'datas': datas})

def my_first_app_detail(request, id):
  data = get_object_or_404(MyFirstModel, pk=id) # pk is the primary key of the data
  return render(request, 'myfirstapp/detail.html', {'data': data})

def review(request):
  reviews = None
  if request.method == 'POST':
    reviewsForm = ReviewForm(request.POST)
    if reviewsForm.is_valid():
      freelancer = reviewsForm.changed_data['freelancer']
      reviews = Tag.objects.filter(freelancers=freelancer)
  else:
    reviewsForm = ReviewForm()
  return render(request, 'myfirstapp/review.html', {'reviews': reviews, 'reviewsForm': reviewsForm})
