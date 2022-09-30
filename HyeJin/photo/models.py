from django.db import models
from django.urls import reverse

from photo.fields import ThumbnailImageField
# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField('One Line Description', max_length=100, blank=True)
    owner = models.ForeignKey('auth.User',on_delete = models.CASCADE,verbose_name='OWNER',blank=True, null=True)
    
    class Meta:
        ordering=('id',)
        
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('photo:album_detail',args=(self.id,))
    
class Photo(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField('TITLE', max_length=40)
    url = models.URLField('URL', unique=True, blank=True, null=True)
    description = models.TextField('Photo Description',blank=True)
    image = ThumbnailImageField(upload_to = 'photo/%Y/%m')
    upload_dt = models.DateTimeField('upload Date', auto_now_add=True)
    owner = models.ForeignKey('auth.User',on_delete = models.CASCADE,verbose_name='OWNER',blank=True, null=True)
    
    class Meta:
        ordering=('title',)
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('photo:photo_detail',args=(self.id,))