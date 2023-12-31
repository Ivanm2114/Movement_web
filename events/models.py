from django.db import models


class PhotoAlbum(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Photo(models.Model):
    image = models.ImageField(blank=True)
    album = models.ForeignKey(PhotoAlbum, null=True, on_delete=models.DO_NOTHING, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        if self.title:
            return self.title
        return self.image.name




class Event(models.Model):
    name = models.CharField(max_length=200)
    short_description = models.CharField(max_length=2000)
    long_description = models.CharField(max_length=2000)
    start_date = models.DateField()
    end_date = models.DateField()
    poster = models.ForeignKey(Photo, on_delete=models.DO_NOTHING, blank=True, related_name='poster', null=True)
    video = models.URLField(blank=True)
    trailer = models.URLField(blank=True)
    amount_of_members = models.IntegerField()
    recent = models.BooleanField()
    photo_album = models.ForeignKey(PhotoAlbum, null=True, on_delete=models.DO_NOTHING, blank=True)
    registration_url = models.URLField(blank=True)
    status = models.CharField(max_length=50)
    partners_event = models.BooleanField()
    logo = models.ForeignKey(Photo, on_delete=models.DO_NOTHING, blank=True, related_name='logo', null=True)
    category = models.CharField(max_length=200, blank=True, null=True)
    vk_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name + ' ' + str(self.start_date.year)


class Person(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    fathers_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    where_knew = models.CharField(max_length=200, blank=True)
    telegram = models.CharField(max_length=200)
    from_hse = models.BooleanField()
    event = models.ForeignKey(Event, on_delete=models.DO_NOTHING)
    university = models.CharField(max_length=200, blank=True, null=True)
    faculty = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.surname + ' ' + self.name + ' ' + self.fathers_name


class Team(models.Model):
    name = models.CharField(max_length=200)
    captain = models.CharField(max_length=200)
    captain_tg = models.CharField(max_length=200)
    captain_email = models.CharField(max_length=200)
    members = models.CharField(max_length=500)
    event = models.ForeignKey(Event, on_delete=models.DO_NOTHING)
    amount_of_members = models.IntegerField()
    where_knew = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name + ' ' + self.event.name


class Sponsor(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ForeignKey(Photo, on_delete=models.DO_NOTHING)
    site_link = models.URLField()

    def __str__(self):
        return self.name


class Head(Person):
    photo = models.ForeignKey(Photo, on_delete=models.DO_NOTHING)
    position = models.CharField(max_length=200)
