from django.db import models
import django.utils.timezone
from django.contrib.auth.models import User

# Create your models here.

USER_PREFERENCES = (
    ('PC', 'Computer'),
    ('TV', 'TV'),
)


class Client(models.Model):
    user = models.OneToOneField(User)
    city = models.CharField(max_length=100)
    preferences = models.CharField(max_length=2, choices=USER_PREFERENCES)


class Topic(models.Model):
    topic_name = models.CharField(max_length=50)

    def return_dict(self):
        return {'pk': self.pk, 'topic_name': self.topic_name}


class Advert(models.Model):
    user = models.ManyToManyField(Client)
    title = models.CharField(max_length=50)
    body = models.TextField()
    date = models.DateTimeField(default=django.utils.timezone.now)
    topic = models.ManyToManyField(Topic)
    archive = models.BooleanField(default=False)
    cost = models.DecimalField(max_digits=15, decimal_places=5)