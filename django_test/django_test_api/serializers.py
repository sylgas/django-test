from rest_framework import serializers

from .models import CallPerson, Connection


class CallPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallPerson
        fields = ('id', 'first_name', 'last_name', )


class ConnectionSerializer(serializers.ModelSerializer):
    init_person = CallPersonSerializer(required=False)
    answer_person = CallPersonSerializer(required=False)

    def get_validation_exclusions(self):
        # Need to exclude `user` since we'll add that later based off the request
        exclusions = super(ConnectionSerializer, self).get_validation_exclusions()
        return exclusions + ['init_person', 'answer_person']
    
    class Meta:
        model = Connection
