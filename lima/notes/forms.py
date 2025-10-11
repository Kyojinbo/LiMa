from django import forms
from . import models

class CreateNote(forms.ModelForm):
    class Meta: #this is specific, needs to be Meta not anything else
        model = models.Note
        fields = ['title', 'body', 'slug', 'tags']
