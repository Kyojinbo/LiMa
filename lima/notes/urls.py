from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    path('', views.notes_list, name='list'),
    path('tag/<str:tag_name>/', views.notes_by_tag, name='tagged_notes'),
    path('notes-home/', views.notes_home, name='home'),
    path('new-note/', views.notes_new, name='new-note'),
    path('<slug:slug>', views.note_page, name='page'), 

]