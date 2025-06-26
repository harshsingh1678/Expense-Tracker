from django.http import HttpResponse # to use HttpResponse
from django.shortcuts import render  # to use render

def home(request):
    # return HttpResponse("hello Project") # to test our project
    return render(request, "website/index.html")
