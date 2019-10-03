from django.shortcuts import render, HttpResponse
# https://github.com/vaisaghvt/django-bot-server-tutorial
from .helper_functions import get_response
from django.utils.safestring import mark_safe
import json

def get_input(request):
    return render(request, 'example.html', {})

def room(request, room_name):
    print(request.method)
    return render(request, 'room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })



# Create your views here.
