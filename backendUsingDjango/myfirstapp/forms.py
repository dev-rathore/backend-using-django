from django import forms
from .models import MyFirstModel

class ReviewForm(forms.Form):
  freelancer = forms.ModelChoiceField(queryset=MyFirstModel.objects.all(), label='Select Freelancer')
  rating = forms.IntegerField()
  comment = forms.CharField(widget=forms.Textarea)
