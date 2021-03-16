from django.shortcuts import render
from .models import Type, Korpus, Kabinet, Techn, History, Profile
from django.contrib.auth.models import User, Group
from django import template
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse
from InvBase.document import TechDocument
from elasticsearch_dsl import Q


register = template.Library()

def mainst(request):
    po = User.objects.all().select_related('profile')
    #po = History.objects.filter(DataPerem__isnull=False).values('IDSotrud__username')
    ty = Type.objects.all()
    ko = Korpus.objects.all()
    return render(request, 'SaveBase/main.html', {'po': po, 'ty': ty, 'ko': ko})

def spisfil(request):
    if 'q' in request.GET:
        #s = TechDocument.search().filter("fuzzy", InvNomer=request.GET['q'])[:30]
        #qs = s.to_queryset()

        q = Q("multi_match", query=request.GET['q'], fields=['InvNomer', 'Naimen'])
        s = TechDocument.search()
        qs = s.query(q)
        return render(request,'SaveBase/spis.html', {'qs' : qs})
    elif 'type' in request.GET:
        q = Q("match", query=request.GET['type'], fields=['TypeTech'])
        s = TechDocument.search()
        qs = s.query(q)
        return render(request,'SaveBase/spis.html', {'qs' : qs})
    else:
        return render(request,'SaveBase/main.html') 

