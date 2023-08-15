from rest_framework import serializers

from .models import Event, Person, PersonNotHSE, Photo, Team, Sponsor, Head, PhotoAlbum


class PhotoAlbumSerializer(serializers.HyperlinkedModelSerializer):
    photos = serializers.SerializerMethodField('get_album_photos')

    def get_album_photos(self, obj):
        return list(x.image.url for x in Photo.objects.filter(album=obj))
    class Meta:
        model = PhotoAlbum
        fields = ['id', 'name', 'photos']


class EventSerializer(serializers.HyperlinkedModelSerializer):
    poster_url = serializers.SerializerMethodField('get_poster_url')

    def get_poster_url(self, obj):
        if obj.poster:
            return obj.poster.image.url
        else:
            return None

    class Meta:
        model = Event
        fields = ['id', 'name',
                  'short_description', 'long_description',
                  'start_date', 'end_date', 'poster', 'poster_url',
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
    logo_url = serializers.SerializerMethodField('get_logo_url')

    def get_logo_url(self, obj):
        if obj.logo:
            return obj.logo.image.url
        else:
            return None

    class Meta:
        model = Sponsor
        fields = ['id', 'name',
                  'logo', 'logo_url', 'site_link']


class HeadSerializer(serializers.HyperlinkedModelSerializer):
    photo_url = serializers.SerializerMethodField('get_photo_url')

    def get_photo_url(self, obj):
        if obj.photo:
            return obj.photo.image.url
        else:
            return None

    class Meta:
        model = Head
        fields = ['id', 'name',
                  'surname', 'fathers_name',
                  'email', 'where_knew',
                  'telegram', 'photo', 'photo_url', 'position']
