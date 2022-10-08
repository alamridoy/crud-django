
from multiprocessing import context
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.db.models import Avg
# Create your views here.


  

def index(request):
  name = Musition.objects.order_by('first_name')
  
  context = {'title':'Home Page','name':name}
  return render(request,'firstapp/index.html',context)



def album_list(request,id):
  artist_info = Musition.objects.get(pk=id)
  list_all = Album.objects.filter(artist=id).order_by('name','release_date')
  num_rating = Album.objects.filter(artist=id).aggregate(Avg('num_star'))
  context = {'title':'Album List','artist_info':artist_info,'list_all':list_all,'num_rating':num_rating}
  return render(request,'firstapp/album_list.html',context)




def musician_form(request):
  musician_form = MusicianForm()
  if request.method == "POST":
    musician_form = MusicianForm(request.POST)
    if musician_form.is_valid():
      musician_form.save(commit=True)
      return index(request)
  context = {'title':'Musician Form','musician_form': musician_form}
  return render(request,'firstapp/musician_form.html',context)




def album_form(request):
  form = AlbumForm()
  if request.method == "POST":
    form = AlbumForm(request.POST)
    if form.is_valid():
      form.save(commit=True)
      return index(request)
  context = {'title':'Album Form','form':form}
  return render(request,'firstapp/album_form.html',context)



def edit_artist(request,id):
  artist_info = Musition.objects.get(pk=id)
  form = MusicianForm(instance=artist_info)
  
  if request.method == "POST":
    form = MusicianForm(request.POST , instance=artist_info)
    if form.is_valid():
      form.save(commit=True)
      return album_list(request,id)
    
  context={'title':'Edit Artist','form': form}
  return render(request,'firstapp/edit_artist.html',context)



def edit_album(request,id):
  album_info = Album.objects.get(pk=id)
  form = AlbumForm(instance=album_info)
  context={}
  if request.method == "POST":
    form = AlbumForm(request.POST,instance=album_info)
    if form.is_valid():
      form.save(commit=True)
      context.update({'success_test': 'Successfylly Updated!'})
      context.update({'id':id})
      # return album_list(request,id)
  context.update({'title':'Edit Album','form':form,'id':id})
  return render(request,'firstapp/edit_album.html',context)



def delete_album(request,id):
  album = Album.objects.get(pk=id).delete()

  context = {'title':'delete album','delete_msg': 'Album deleted successfull!'}
  
  return render(request,'firstapp/delete.html',context)