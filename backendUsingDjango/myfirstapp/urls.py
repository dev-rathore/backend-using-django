from django.urls import path
from . import views

# localhost:8080/myfirstapp/
urlpatterns = [
  path('', views.my_first_app, name='my_first_app'),
  path('<int:id>/', views.my_first_app_detail, name='my_first_app_detail'),
]
