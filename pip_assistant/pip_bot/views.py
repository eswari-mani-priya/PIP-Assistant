from django.shortcuts import render, HttpResponse

def get_input(request):
    return render(request, template_name="chatbox.html")


# Create your views here.
