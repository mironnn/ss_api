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

    def return_dict(self):
        return {'user': self.user.id,
                'username': self.user.username,
                'first_name': self.user.first_name,
                'last_name': self.user.last_name,
                'email': self.user.email,
                'city': self.city,
                'preferences': self.preferences
                }

    def get_username(self):
        return self.user.username


class Topic(models.Model):
    topic_name = models.CharField(max_length=50)

    def return_dict(self):
        return {'id': self.id,
                'topic_name': self.topic_name}


class Advert(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=50)
    body = models.TextField()
    date = models.DateTimeField(default=django.utils.timezone.now)
    topic = models.ManyToManyField(Topic, blank=True)
    archive = models.BooleanField(default=False)
    cost = models.DecimalField(max_digits=15, decimal_places=2)

    def return_dict(self):
        return {'user': self.user.pk,
                'title': self.title,
                'body': self.body,
                'date': self.date.strftime("%d.%m.%Y"),
                'topic': [topic.topic_name for topic in self.topic.all()],
                'archive': self.archive,
                'cost': str(self.cost),
                }