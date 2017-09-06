from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<h1>Hola Mundo!! :)</h1>")

def saludo(request, saludo):
    greetings = "<b>Hola %s como estas? :)</b>" % saludo
    # print('Desde saludo :)')
    return HttpResponse(greetings)