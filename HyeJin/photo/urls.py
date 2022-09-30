from django.urls import path
from photo import views

app_name='photo'
urlpatterns = [
    # Example : /photo/
    path('',views.AlbumLV.as_view(),name="index"),
    
    # Example : /photo/album/, same as /photo/
    path('album',views.AlbumLV.as_view(),name="album_list"),
    
    # Example : /photo/album/99
    path('album/<int:pk>/',views.AlbumDV.as_view(),name="album_detail"),
    
    # Example : /photo/photo/99
    path('photo/<int:pk>/',views.PhotoDV.as_view(),name="photo_detail"),
    
    path('album/add/',views.AlbumCV.as_view(),name='album_add'),
    path('album/change/',views.AlbumChangeLV.as_view(),name='album_change'),
    path('album/<int:pk>/update/',views.AlbumUV.as_view(),name='album_update'),
    path('album/<int:pk>/delete/',views.AlbumDelV.as_view(),name='album_delete'),
    
    path('photo/add/',views.PhotoCV.as_view(),name='photo_add'),
    path('photo/change/',views.PhotoChangeLV.as_view(),name='photo_change'),
    path('photo/<int:pk>/update/',views.PhotoUV.as_view(),name='photo_update'),
    path('photo/<int:pk>/delete/',views.PhotoDelV.as_view(),name='photo_delete'),

]