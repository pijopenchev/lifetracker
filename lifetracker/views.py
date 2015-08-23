from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from lifetracker.models import User, Note
import logging
# Create your views here.

USER_ID = 1
logger = logging.getLogger(__name__)

def index(request, message=''):
    return render(request, "index.html", {'message': message})

def getUsers(request):
    users = User.objects.all()
    return render(request, "getUsers.html", {'users': users})

def getUser(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        raise Http404("User does not exist.")
    context = {
        'user': user
    }
    return render(request, "getUser.html", context)

def getNote(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    return render(request, "getNote.html", {'note': note})


def addNote(request):
    logger.error("HI")
    newNote = request.POST['newNote']
    if newNote == '':
        message = "Empty notes not allowed."
    else:
        user = User.objects.get(id=USER_ID)
        note = Note(user=user, body=newNote)
        note.save()
        message = "Note added successfully."

    return render(request, 'index.html', {'message': message})






