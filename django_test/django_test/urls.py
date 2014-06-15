from django.conf.urls import patterns, include, url

from django.contrib import admin
from django_test.views import index, static

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin', include(admin.site.urls)),
                       url(r'^api/', include('django_test_api.urls')),
                       url(r'^(?P<template_name>\w+)$', static, name='template'),
                       url(r'^$', index, name='index'),
)

