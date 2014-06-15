__author__ = 'Sylgas'

from django.conf.urls import patterns, include, url
from django_test_api import views

connection_urls = patterns('',
                           url(r'^$', views.connections, name='connection_list')
)

person_urls = patterns('',
                       url(r'^/(?P<id>\d+)/connection$', include(connection_urls)),
                       url(r'^/create', views.create_person, name='create_person'),
                       url(r'^$', views.index, name='person_list')
)

urlpatterns = patterns('',
                       url(r'^person', include(person_urls)),
)
