from datetime import date
from platform import release
from tkinter import Widget
from django.db import models

# Create your models here.

class Musition(models.Model):
  #id = models.AutoField(primary_key=True)
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  instrument =models.CharField(max_length=100)
  
  def __str__(self) -> str:
    return self.first_name+ " "+ self.last_name
  
  
class Album(models.Model):
  artist = models.ForeignKey(Musition,on_delete=models.CASCADE)
  name = models.CharField(max_length=100)
  release_date = models.DateField()
  
  rating = (
    (1, "Worst"),
    (2, "Bad"),
    (3, "Not Bad"),
    (4, "Good"),
    (5, "Excellent"),
  )
  num_star = models.IntegerField(choices=rating)
  
  def __str__(self) -> str:
    return self.name+" "+ f'rating is {self.num_star.name}'
  
  
  