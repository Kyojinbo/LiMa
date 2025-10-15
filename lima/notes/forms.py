from django import forms
from . import models

#class CreateNote(forms.ModelForm):
    #class Meta: #this is specific, needs to be Meta not anything else
        #model = models.Note
        #fields = ['title', 'body', 'slug', 'tags']


class NoteForm(forms.ModelForm):
    tag_input = forms.CharField(required=False, label="Tags (comma-separated)", widget=forms.TextInput(attrs={'placeholder': 'e.g. work, ideas'}))

    class Meta:
        model = models.Note
        fields = ['title', 'body', 'slug', 'tag_input']

    def save(self, commit=True, user=None):
        note = super().save(commit=False)
        if user:
            note.user = user
        
        if commit or not note.pk:
            note.save()

        #process tags
        tag_names = self.cleaned_data['tag_input'].split(',')
        tag_names = [name.strip() for name in tag_names if name.strip()]

        for tag_name in tag_names:
            tag_obj, created = models.Tag.objects.get_or_create(name=tag_name)
            note.tags.add(tag_obj)
        return note