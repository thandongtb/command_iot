from django.shortcuts import render
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.template import loader
# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context=None, request=request))
