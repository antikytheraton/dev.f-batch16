from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sum(request, num1):
    resultado = num1 + num1
    return HttpResponse("<h1>Suma de 3 + 5: %s </h1>" % resultado)

def mult(request):
    resultado = 5 * 5
    return HttpResponse("<h1>Multiplo de 5 * 5 : %s</h1>" % resultado)