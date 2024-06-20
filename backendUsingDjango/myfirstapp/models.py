from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class MyFirstModel(models.Model): # Freelancer
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

# One to Many Relationship
class Review(models.Model):
  freelancer = models.ForeignKey(MyFirstModel, on_delete=models.CASCADE, related_name='reviews')
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  rating = models.IntegerField()
  comment = models.TextField()
  date_added = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return f'{self.freelancer.name} serving for {self.user.username}'

# Many to Many Relationship
class Tag(models.Model):
  name = models.CharField(max_length=100)
  location = models.CharField(max_length=100)
  freelancers = models.ManyToManyField(MyFirstModel, related_name='tags')

  def __str__(self):
    return self.name

# One to One Relationship
class Certificate(models.Model):
  freelancer = models.OneToOneField(MyFirstModel, on_delete=models.CASCADE, related_name='certificate')
  certificate_name = models.CharField(max_length=100)
  issued_date = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return f'{self.freelancer.name} is a certified freelancer'
