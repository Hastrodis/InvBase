from django.conf.urls import url
from django.urls import path, re_path, include
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    url(r'^$', views.mainst, name='main'),
    url(r'^spis/$', views.spisfil, name='spisfil'),
    path('sver/', include('xlsPars.urls')),
]
