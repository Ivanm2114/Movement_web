from rest_framework import serializers

from .models import Event, Person, PersonNotHSE, Photo, Team, Video, Sponsor, Head


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


class SponsorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sponsor
        fields = '__all__'


class VideoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'


class HeadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Head
        fields = '__all__'
