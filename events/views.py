from django.http import HttpResponse
from rest_framework import viewsets

from .serializers import PhotoSerializer, PersonSerializer, \
    PersonNotHSESerializer, TeamSerializer, EventSerializer, \
    HeadSerializer, SponsorSerializer, VideoSerializer
from .models import Person, PersonNotHSE, \
    Photo, Event, Team, Sponsor, Head, Video


def index(request):
    return HttpResponse("Hello, world. You're at the events index.")


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all().order_by('name')
    serializer_class = PersonSerializer


class PersonNotHSEViewSet(viewsets.ModelViewSet):
    queryset = PersonNotHSE.objects.all()
    serializer_class = PersonNotHSESerializer


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


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


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
