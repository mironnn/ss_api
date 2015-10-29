import json
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from models_first.validators import validate
from models_first.models import Topic, Client, Advert


def get_model_filter_values(request, model):
    """
    Create values for model filter
    :param request: request with attributes
    :param model: model class for which we creates filter
    :return: keys and values for model filter: dict with attributes and values from request GET
    """
    kwargs = {key: val for key, val in request.GET.items()}
    return validate(kwargs, [field.name for field in model._meta.get_fields()])


def home(request):
    return HttpResponse('ok')


def users(request):

    if request.method == 'GET':

        values = get_model_filter_values(request, Client)

        if values:
            try:
                clients = [advert.return_dict() for advert in Client.objects.filter(**values)]
            except ValueError:
                return HttpResponse(status=400)
        else:
            clients_obj = Client.objects.all()
            clients = [client.return_dict() for client in clients_obj]
        data = {'users': clients}
        return HttpResponse(json.dumps(data), content_type='application/json')


@csrf_exempt
def topics(request, id=None):

    if request.method == 'GET':

        values = get_model_filter_values(request, Topic)

        if values:
            try:
                topics = [advert.return_dict() for advert in Topic.objects.filter(**values)]
            except ValueError:
                return HttpResponse(status=400)
        else:
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

    if request.method == 'PUT' and id:
        '''
        waiting json like: {"topic_name": "postman2"}
        '''
        try:
            update_topic = Topic.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse(status=400)
        try:
            received_data = json.loads((request.body).decode('utf-8'))['topic_name']
        except (KeyError, ValueError):
            return HttpResponse(status=400)
        else:
            update_topic.topic_name = received_data
            update_topic.save()
            data = {'new_topic': update_topic.return_dict()}
            return HttpResponse(json.dumps(data), content_type='application/json')

    if request.method == 'DELETE' and id:
        try:
            del_topic = Topic.objects.get(id=id)
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
        '''
        waiting url for example:
        http://127.0.0.1:8100/api/adverts/?user=2
        http://127.0.0.1:8100/api/adverts/?topic=3&user=2
        '''

        values = get_model_filter_values(request, Advert)

        if values:
            try:
                adverts = [advert.return_dict() for advert in Advert.objects.filter(**values)]
            except (ValueError, ValidationError):
                return HttpResponse(status=400)
        else:
            adverts_obj = Advert.objects.all()
            adverts = [advert.return_dict() for advert in adverts_obj]

        data = {'adverts': adverts}
        return HttpResponse(json.dumps(data), content_type='application/json')

    if request.method == 'POST':
        '''
        {"id": "2", "cost": "6", "title": "postman_title", "body": "postman_body"}
        '''
        try:
            received_data = json.loads((request.body).decode('utf-8'))
        except ValueError:
            return HttpResponse(status=400)
        try:
            user_obj = User.objects.get(id=received_data.get('id'))
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
