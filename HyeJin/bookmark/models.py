from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Bookmark(models.Model):
    title = models.CharField('TITLE', max_length=100, blank=True)
    url = models.URLField('URL', unique=True)
    content = models.TextField('CONTENT', default="내용이 없습니다.")
    owner = models.ForeignKey(User, on_delete = models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.title
    