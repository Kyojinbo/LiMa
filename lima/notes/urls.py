from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    path('', views.notes_list, name='list'),
    path('<slug:slug>', views.note_page, name='page'), 

]