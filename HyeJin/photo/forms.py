from django.forms import inlineformset_factory
from .models import *

PhotoInlineFormSet=inlineformset_factory(Album,
                                         Photo,
                                         fields = ['image', 'title','url', 'description'],
                                         extra = 2
                                         )