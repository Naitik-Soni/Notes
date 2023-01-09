from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def notes(request):
    allnotes = Notes.objects.all().values()
    return render(request, "notes.html", {"mynotes": allnotes})

def addnotes(request):
    title = request.POST['title']
    note = request.POST['thisnote']
    notes = Notes(title = title, notecontent = note)
    notes.save()
    return HttpResponseRedirect(reverse("notes"))

def updatenotes(request, id):
    thisnote = Notes.objects.get(id = id)
    title = request.POST['title']
    note = request.POST['thisnote']
    thisnote.title = title
    thisnote.notecontent = note
    thisnote.save()
    return HttpResponseRedirect(reverse("notes"))

def delete(request, id):
    note = Notes.objects.get(id = id)
    note.delete()
    return HttpResponseRedirect(reverse("notes"))