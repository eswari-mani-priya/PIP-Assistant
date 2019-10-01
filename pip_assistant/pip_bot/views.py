from django.shortcuts import render, HttpResponse
from .helper_functions import get_response

def get_input(request):
    print(request.POST)
    input = request.POST.get('utext',False)
    print("input:",input)
    output=None
    if input:
        output = get_response(input)
        print("UserInput:",input,"BotOut:",output)
    return render(request, "chatbox.html", {'output': output})


# Create your views here.
