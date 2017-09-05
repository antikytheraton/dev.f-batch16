from django.conf.urls import url, include
from .views import sum, mult

urlpatterns = [
    url(r'^sum/(?P<num1>\[0-9+])/$', sum),
    url(r'^mult/', mult),
    # url(r'^sum/(?P<num1>\w+)/$', sum)
]