from django.contrib import admin

from .models import Person, PersonNotHSE, Team, Photo, Event, Head, Sponsor, Video

admin.site.register(Person)
admin.site.register(PersonNotHSE)
admin.site.register(Team)
admin.site.register(Photo)
admin.site.register(Event)
admin.site.register(Head)
admin.site.register(Sponsor)
admin.site.register(Video)
# Register your models here.
