from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.utils import simplejson
from django.template import RequestContext

def home(request):
    context = RequestContext(request)
    
    data = dict()
    return render_to_response("index.html", data, context)
    
