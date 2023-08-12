from rest_framework import serializers

from .models import Event, Person, PersonNotHSE, Photo, Team, Sponsor, Head, PhotoAlbum


class PhotoAlbumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PhotoAlbum
        fields = ['id','name']


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'name',
                  'short_description', 'long_description',
                  'start_date', 'end_date', 'poster',
                  'video', 'trailer',
                  'amount_of_members', 'recent',
                  'photo_album', 'registration_url',
                  'status', 'partners_event']


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'name',
                  'surname', 'fathers_name',
                  'email', 'where_knew', 'telegram']


class PersonNotHSESerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonNotHSE
        fields = ['id', 'name',
                  'surname', 'fathers_name',
                  'email', 'where_knew', 'telegram', 'pass_ready']


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name',
                  'captain', 'members',
                  'event', 'amount_of_members']


class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Photo
        fields = ['id', 'image',
                  'album', 'title']


class SponsorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sponsor
        fields = ['id', 'name',
                  'logo', 'site_link']


class HeadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Head
        fields = ['id', 'name',
                  'surname', 'fathers_name',
                  'email', 'where_knew',
                  'telegram', 'photo', 'position']
