from django.shortcuts import render
from django import template
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse

register = template.Library()

# Create your views here.
def sver(request):
     return render(request,'xlsPars/sver.html')