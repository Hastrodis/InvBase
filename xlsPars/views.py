from django.shortcuts import render
from django import template
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse
from SaveBase.models import Techn
from .pars import pars

register = template.Library()

# Create your views here.
def sver(request):
     pro = Techn.objects.all().values('InvNomer','Naimen','IDUser__last_name')
     result = pars(pro) #procedura parsinga
     return render(request,'xlsPars/sver.html', {'result':result})