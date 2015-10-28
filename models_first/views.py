import json
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt

from models_first.models import Topic


def home(request):
    return HttpResponse('ok')


@csrf_exempt
def topics(request, pk=None):

    if request.method == 'GET':
        topics_obj = Topic.objects.all()
        topics = [topic.return_dict() for topic in topics_obj]
        data = {'topics': topics}
        return HttpResponse(json.dumps(data), content_type='application/json')

    if request.method == 'POST':
        '''
        waiting json like: {"topic_name": "postman2"}
        '''
        try:
            received_data = json.loads((request.body).decode('utf-8'))['topic_name']
        except KeyError:
            return HttpResponse(status=400)
        else:
            new_topic = Topic(topic_name=received_data)
            new_topic.save()
            data = {'new_topic': new_topic.return_dict()}
            return HttpResponse(json.dumps(data), content_type='application/json')

    if request.method == 'PUT' and pk:
        '''
        waiting json like: {"topic_name": "postman2"}
        '''
        try:
            update_topic = Topic.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return HttpResponse(status=400)
        try:
            received_data = json.loads((request.body).decode('utf-8'))['topic_name']
        except KeyError:
            return HttpResponse(status=400)
        else:
            update_topic.topic_name = received_data
            update_topic.save()
            data = {'new_topic': update_topic.return_dict()}
            return HttpResponse(json.dumps(data), content_type='application/json')

    if request.method == 'DELETE' and pk:
        try:
            del_topic = Topic.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return HttpResponse(status=400)
        else:
            del_topic.delete()
            return HttpResponse(status=200)

    else:
        return HttpResponse(status=400)
