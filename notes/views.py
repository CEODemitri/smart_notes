from django.shortcuts import render
from django.http import Http404
from django.views.generic import CreateView, DetailView, ListView, UpdateView

# Create your views here.
from .forms import NotesForm
from .models import Notes

class NotesUpdatView(UpdateView):
    model: Notes
    # fields: ['title', 'text']
    success_url = '/smart/notes'
    form_class = NotesForm

class NotesCreateView(CreateView):
    model: Notes
    # fields: ['title', 'text']
    success_url = '/smart/notes'
    form_class = NotesForm
    

class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"

class NotesDetailsView(DetailView):
    model = Notes
    context_object_name = "note"


def detail(request, pk):
    try:
        note = Notes.object.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404("Note does not exist in this realm")
    return render(request, 'notes/notes_detail.html', {'note': note})