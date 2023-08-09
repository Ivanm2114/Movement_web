from rest_framework import serializers

from .models import Event, Person, PersonNotHSE, Photo, Team


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class PersonNotHSESerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonNotHSE
        fields = '__all__'


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'

