from django.contrib import admin

from .models import Person, Team, Photo, Event, Head, Sponsor, PhotoAlbum

admin.site.register(Person)
admin.site.register(Team)
admin.site.register(Photo)
admin.site.register(Event)
admin.site.register(Head)
admin.site.register(Sponsor)
admin.site.register(PhotoAlbum)
# Register your models here.
