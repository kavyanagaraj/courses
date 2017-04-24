from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.process),
    url(r'^courses/delete/(?P<id>\d+)$', views.delete),
    url(r'^delprocess/(?P<id>\d+)$', views.delprocess)
]
