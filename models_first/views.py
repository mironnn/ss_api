import json

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, Http404

from models_first.models import Topic



def home(request):
    return HttpResponse('ok')


def api_topics(request):

    if request.method == 'GET':
        topics_obj = Topic.objects.all()
        topics = [model_to_dict(topic) for topic in topics_obj]
        print (topics)
        data = {'topics': topics}
        return HttpResponse(json.dumps(data), content_type='application/json')