from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .helper_functions import get_response
import json


@csrf_exempt
def get_output(request):
    response = {'status': None}
    if request.method == 'POST':
        data = json.loads(request.body)
        message = data['message']
        chat_response = get_response(message)
        response['message'] = {'text': chat_response, 'user':False, 'chat_bot':True}
        response['status'] = 'ok'
    else:
        response['error'] = 'no post data found'
    return HttpResponse(json.dumps(response), content_type="application/json")


def home(request, template_name="chathome.html"):
    context = {'title': 'PIP BOT Version 1.0'}
    return render_to_response(template_name, context)




