from django.shortcuts import render, redirect, get_object_or_404
from .models import Note, Tag
from django.contrib.auth.decorators import login_required
from . import forms
from .forms import NoteForm


# Create your views here.
@login_required(login_url='/users/login')
def notes_home(request):
    return render(request, 'notes/notes_home.html')

@login_required(login_url='/users/login/')
def notes_list(request):
    notes = Note.objects.filter(user=request.user).order_by('-date')
    return render(request, 'notes/notes_list.html', {'notes': notes})

@login_required(login_url='/users/login/')
def note_page(request, slug):
    note = get_object_or_404(Note, slug=slug) #gets the one slug we have that matches thje slug we are given. is info passed around to identify what this is
    return render(request, 'notes/notes_page.html', {'note': note})

def notes_new(request):
    if request.method=="POST":
        form = forms.NoteForm(request.POST, request.FILES)
        if form.is_valid():
            newnote = form.save(user=request.user)
            return redirect('notes:list')
    else:
        form = forms.NoteForm()
    return render(request, 'notes/notes_new.html', {'form':form})

@login_required(login_url='/users/login/')
def notes_by_tag(request, tag_name):
    tag = get_object_or_404(Tag, name=tag_name)
    notes = Note.objects.filter(user=request.user, tags=tag)
    return render(request, 'notes/notes_by_tag.html', {
        'notes': notes,
        'tag_filter': tag.name,
    })

@login_required(login_url='/users/login/')
def create_note(request):
    if request.method=="POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save(user=request.user)
            return redirect('notes:home')
    else:
        form = NoteForm()

    return render(request, 'notes/notes_new.html', {'form': form})