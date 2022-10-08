from dataclasses import fields
from pyexpat import model
from django import forms
from django.core import validators
from .models import *

class MusicianForm(forms.ModelForm):
  class Meta:
    model = Musition
    fields = '__all__'


class AlbumForm(forms.ModelForm):
  release_date = forms.DateField(widget=forms.TextInput(attrs={'type':'date'}))
  class Meta:
    model = Album
    fields = '__all__'