from django.shortcuts import render_to_response
from django.template import RequestContext

def home(request,template="demo/demo.html"):
    return render_to_response(template,
                              {},
                              context_instance=RequestContext(request))
