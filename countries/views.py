from django.http import HttpResponse
from django.utils import simplejson


def countries_lookup(request):
    return_value = [{'name':'United States','code':'US'},{'name':'England','code':'EN'}, 
                    {'name':'Indonesia','code':'ID'}]
    json = simplejson.dumps(return_value)
    return HttpResponse(json,
                        mimetype="application/json")

def cities_lookup(request):
    json = simplejson.dumps({})
    return HttpResponse(json,
                        mimetype="application/json")
