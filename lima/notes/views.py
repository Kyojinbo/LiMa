from django.shortcuts import render
from .models import Note


# Create your views here.
def notes_list(request):
    notes = Note.objects.all().order_by('-date')
    return render(request, 'notes/notes_list.html', {'notes': notes})

def note_page(request, slug):
    note = Note.objects.get(slug=slug) #gets the one slug we have that matches thje slug we are given. is info passed around to identify what this is
    return render(request, 'notes/note_page.html', {'note': note})