from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    fathers_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)


class PersonNotHSE(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    pass_ready = models.BooleanField()


class Team(models.Model):
    captain = models.ForeignKey(Person, on_delete=models.DO_NOTHING)
    members = models.CharField(max_length=500)


class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    poster = models.ImageField()
    telegram_URL = models.URLField()


class Photo(models.Model):
    image = models.ImageField()
    event = models.ForeignKey(Event, on_delete=models.DO_NOTHING)
