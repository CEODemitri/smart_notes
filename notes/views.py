from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import Http404
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from .forms import NotesForm
from .models import Notes

class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes'
    template_name = 'notes/notes_delete.html'

class NotesUpdateView(UpdateView):
    model: Notes
    # fields: ['title', 'text']
    success_url = '/smart/notes'
    form_class = NotesForm

class NotesCreateView(CreateView):
    model: Notes
    # fields: ['title', 'text']
    success_url = '/smart/notes'
    form_class = NotesForm
    

class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"
    login_url = "/admin"

    def get_queryset(self):
        return self.request.user.notes.all()

class NotesDetailsView(DetailView):
    model = Notes
    context_object_name = "note"


def detail(request, pk):
    try:
        note = Notes.object.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404("Note does not exist in this realm")
    return render(request, 'notes/notes_detail.html', {'note': note})