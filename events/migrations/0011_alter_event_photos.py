# Generated by Django 4.2.4 on 2023-08-12 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_alter_event_photos_alter_event_poster_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='photos',
            field=models.ManyToManyField(blank=True, related_name='photos', to='events.photo'),
        ),
    ]
