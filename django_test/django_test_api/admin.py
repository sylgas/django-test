from django.contrib import admin
from django_test_api.models import CallPerson, Connection

# Register your models here.

#python manage.py diffsetting
#if settings.DEBUG:
    # Do something
    #settings.configure(DEBUG=True, TEMPLATE_DEBUG=True,
    #TEMPLATE_DIRS=('/home/web-apps/myapp', '/home/web-apps/base'))

admin.site.register(CallPerson)
admin.site.register(Connection)