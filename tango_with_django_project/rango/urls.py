from django.conf.urls import url
from rango import views

urlpatters = [
    url(r'^$', views.index, name='index'),
]

