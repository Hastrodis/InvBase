from django.shortcuts import render
from .models import Type, Korpus, Kabinet, Techn, History
from django.contrib.auth.models import User, Group
from django import template
from django.http import HttpResponseRedirect, HttpResponseNotFound

register = template.Library()

def mainst(request):
    po = History.objects.filter(DataPerem__isnull=False).values('IDSotrud__username')
    ty = Type.objects.all()
    ko = Korpus.objects.all()
    return render(request, 'SaveBase/main.html', {'po': po, 'ty': ty, 'ko': ko})

def spisfil(request):
    return render(request,'SaveBase/spis.html')