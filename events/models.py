from django.db import models


class Photo(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=200)


class Video(models.Model):
    video = models.FileField()
    title = models.CharField(max_length=200)


class Event(models.Model):
    name = models.CharField(max_length=200)
    short_description = models.CharField(max_length=2000)
    long_description = models.CharField(max_length=2000)
    start_date = models.DateTimeField()
    start_year = models.IntegerField()
    end_date = models.DateTimeField()
    end_year = models.IntegerField()
    poster = models.ImageField()
    video = models.FileField()
    trailer = models.FileField()
    amount_of_members = models.IntegerField()
    recent = models.BooleanField()
    photos = models.ManyToManyField(Photo)

    def __str__(self):
        return self.name + ' ' + str(self.start_date.year)


class Person(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    fathers_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    where_knew = models.CharField(max_length=200)
    telegram = models.CharField(max_length=200)

    def __str__(self):
        return self.surname + ' ' + self.name + ' ' + self.fathers_name


class PersonNotHSE(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    pass_ready = models.BooleanField()

    def __str__(self):
        return self.person.surname + ' ' + self.person.name + ' ' + self.person.fathers_name


class Team(models.Model):
    name = models.CharField(max_length=200)
    captain = models.ForeignKey(Person, on_delete=models.DO_NOTHING)
    members = models.CharField(max_length=500)
    event = models.ForeignKey(Event, on_delete=models.DO_NOTHING)
    amount_of_members = models.IntegerField()

    def __str__(self):
        return self.name + ' ' + self.event.name


class Sponsor(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField()
    url = models.URLField()

    def __str__(self):
        return self.name


class Head(Person):
    photo = models.ImageField()
    position = models.CharField(max_length=200)

