import json
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt

from models_first.models import Topic, Client, Advert


def home(request):
    return HttpResponse('ok')


def users(request):

    if request.method == 'GET':
        clients_obj = Client.objects.all()
        clients = [client.return_dict() for client in clients_obj]
        data = {'users': clients}
        return HttpResponse(json.dumps(data), content_type='application/json')


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
        except (KeyError, ValueError):
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

@csrf_exempt
def adverts(request):

    if request.method == 'GET':
        adverts_obj = Advert.objects.all()
        adverts = [advert.return_dict() for advert in adverts_obj]
        data = {'adverts': adverts}
        return HttpResponse(json.dumps(data), content_type='application/json')

    if request.method == 'POST':
        '''
        {"pk": "2", "cost": "6", "title": "postman_title", "body": "postman_body"}
        '''
        try:
            received_data = json.loads((request.body).decode('utf-8'))
        except ValueError:
            return HttpResponse(status=400)
        try:
            user_obj = User.objects.get(pk=received_data.get('pk'))
        except ObjectDoesNotExist:
            return HttpResponse(status=400)
        else:
            new_advert = Advert.objects.create(user=user_obj,
                                               title=received_data.get('title'),
                                               body=received_data.get('body'),
                                               cost=received_data.get('cost'),
                                               )
            data = {'new_topic': new_advert.return_dict()}
            return HttpResponse(json.dumps(data), content_type='application/json')

    else:
        return HttpResponse(status=400)