from django.urls import path
from .views import *
urlpatterns = [
    path('',index, name='index'),
    path('album_list/<int:id>/',album_list, name='album_list'),
    path('musician_form/',musician_form, name='musician_form'),
    path('album_form/',album_form, name='album_form'),
    path('edit_artist/<int:id>/', edit_artist, name='edit_artist'),
    path('edit_album/<int:id>/', edit_album, name='edit_album'),
    path('delete_album/<int:id>/',delete_album,name='delete_album'),
]
