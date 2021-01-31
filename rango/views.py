from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Rango says hey there partner.Rango says hey there partner! <br/> < a href=' '>About</ a>.")
def index(about):
    return HttpResponse("Rango says here is the about page！< a href=" ">Index</ a>")