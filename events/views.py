import json

from django.http import HttpResponse, FileResponse
from django.views.generic import DetailView
from rest_framework import viewsets

from .serializers import PhotoSerializer, PersonSerializer, \
    PersonNotHSESerializer, TeamSerializer, EventSerializer, \
    HeadSerializer, SponsorSerializer, PhotoAlbumSerializer
from .models import Person, PersonNotHSE, \
    Photo, Event, Team, Sponsor, Head, PhotoAlbum


def index(request):
    return HttpResponse("Hello, world. You're at the events index.")


class PhotoAlbumViewSet(viewsets.ModelViewSet):
    queryset = PhotoAlbum.objects.all()
    serializer_class = PhotoAlbumSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all().order_by('name')
    serializer_class = PersonSerializer


class PersonNotHSEViewSet(viewsets.ModelViewSet):
    queryset = PersonNotHSE.objects.all()
    serializer_class = PersonNotHSESerializer


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    def post(self, request, *args, **kwargs):
        file = request.data['file']
        image = Photo.objects.create(image=file)
        return HttpResponse(json.dumps({'message': "Uploaded"}), status=200)


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class SponsorViewSet(viewsets.ModelViewSet):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer


class HeadViewSet(viewsets.ModelViewSet):
    queryset = Head.objects.all()
    serializer_class = HeadSerializer
