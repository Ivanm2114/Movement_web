from django.urls import path, include
from rest_framework import routers
from django.http import FileResponse

from . import views

router = routers.DefaultRouter()
router.register(r'person', views.PersonViewSet)
router.register(r'photo', views.PhotoViewSet)
router.register(r'team', views.TeamViewSet)
router.register(r'event', views.EventViewSet)
router.register(r'photoalbum', views.PhotoAlbumViewSet)
router.register(r'sponsor', views.SponsorViewSet)
router.register(r'head', views.HeadViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
