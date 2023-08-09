from django.contrib import admin

from .models import Person, PersonNotHSE, Team, Photo, Event

admin.site.register(Person)
admin.site.register(PersonNotHSE)
admin.site.register(Team)
admin.site.register(Photo)
admin.site.register(Event)
# Register your models here.
