from django.shortcuts import render, HttpResponse
from .helper_functions import get_response

def get_input(request):
    input = request.POST.get('utext',False)
    if input:
        output = get_response(input)
        print("UserInput:",input,"BotOut:",output)
    return render(request, template_name="chatbox.html")


# Create your views here.
