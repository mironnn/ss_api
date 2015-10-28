# coding: utf-8
from django.conf.urls import patterns, url

__author__ = 'sever'

urlpatterns = patterns('models_first.views',
    url(r'^home/$', 'home', name='test_home'),

    #topics
    url(r'^topics/$', 'topics', name='get_topics'),
    url(r'^topics/(?P<pk>\d+)$', 'topics', name='update_topic'),

)