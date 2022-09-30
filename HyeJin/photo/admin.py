from django.contrib import admin
from photo.models import Album, Photo

# Register your models here.
class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 2
    
@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    inlines = (PhotoInline,)
    list_display = ('id','name','description')
     
@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id','title','url','upload_dt')