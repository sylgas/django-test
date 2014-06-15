from rest_framework import permissions, generics
from .models import CallPerson, Connection
from .serializers import CallPersonSerializer, ConnectionSerializer
from django.db.models import Q

# Create your views here.

class CreatePersonPageView(generics.CreateAPIView):
    model = CallPerson
    serializer_class = CallPersonSerializer

    permission_classes = [
        permissions.AllowAny
    ]


class IndexPageView(generics.ListAPIView):
    model = CallPerson
    serializer_class = CallPersonSerializer

    permission_classes = [
        permissions.AllowAny
    ]


def get_queryset(self):
    return CallPerson.objects.all()


class ConnectionListView(generics.ListAPIView):
    model = Connection
    serializer_class = ConnectionSerializer

    permission_classes = [
        permissions.AllowAny
    ]

    def get_queryset(self):
        person_id = self.kwargs.get('id')
        return Connection.objects.filter(Q(init_person=person_id) | Q(answer_person=person_id))


create_person = CreatePersonPageView.as_view()
index = IndexPageView.as_view()
connections = ConnectionListView.as_view()
