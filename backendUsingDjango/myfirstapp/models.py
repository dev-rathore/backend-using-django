from django.db import models
from django.utils import timezone

# Create your models here.
class MyFirstModel(models.Model):
  OCCUPATION_CHOICES = [
    ('S', 'Student'),
    ('T', 'Teacher'),
    ('D', 'Developer'),
    ('O', 'Other'),
  ]
  name = models.CharField(max_length=100)
  image = models.ImageField(upload_to='images/')
  date_added = models.DateTimeField(default=timezone.now)
  occupation = models.CharField(max_length=1, choices=OCCUPATION_CHOICES)
  description = models.TextField(default='')

  def __str__(self):
    return self.name
