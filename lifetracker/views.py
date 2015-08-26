from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from lifetracker.models import Note
from django.contrib.auth.models import User
import logging
# Create your views here.

logger = logging.getLogger(__name__)

@login_required
def index(request, message=''):
    return render(request, "index.html", {'message': message})

@login_required
def getUsers(request):
    users = User.objects.all()
    return render(request, "getUsers.html", {'users': users})
@login_required
def getUser(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        raise Http404("User does not exist.")
    context = {
        'user': user
    }
    return render(request, "getUser.html", context)
@login_required
def getNote(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    return render(request, "getNote.html", {'note': note})

@login_required
def addNote(request):
    logger.error("HI")
    newNote = request.POST['newNote']
    if newNote == '':
        message = "Empty notes not allowed."
    else:
        user = request.user
        note = Note(user=user, body=newNote)
        note.save()
        message = "Note added successfully."

    return render(request, 'index.html', {'message': message})






