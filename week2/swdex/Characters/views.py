from django.shortcuts import render
import requests
# Create your views here.

def index(request,pagina=1):
    req = requests.get("http://swapi.co/api/people/?page={0}".format(pagina))
    if req.status_code == 200:
        characters = req.json()['results']
    else:
        characters = []
    return render(request,'characters/index.html',{'personajes':characters})