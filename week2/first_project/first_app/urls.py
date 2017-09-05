'''
    Urls del app
    Se considera buena practica que cada app tenga su urls.py
'''
from django.conf.urls import url
from .views import index, saludo

urlpatterns = [
    url(r'^$', index),
    url(r'^saludo/(?P<saludo>\w+)/$', saludo),
]
