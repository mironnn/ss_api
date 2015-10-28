import json

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from models_first.models import Topic


def home(request):
    return HttpResponse('ok')


def api_topics(request):

    if request.method == 'GET':
        topics_obj = Topic.objects.all()
        topics = [topic.return_dict() for topic in topics_obj]
        data = {'topics': topics}
        return HttpResponse(json.dumps(data), content_type='application/json')


@csrf_exempt
def create_topic(request):

    if request.method == 'POST':
        new_topic = Topic(topic_name=request.POST.get('topic_name'))
        new_topic.save()
        data = {'new_topic': new_topic.return_dict()}
        return HttpResponse(json.dumps(data), content_type='application/json')