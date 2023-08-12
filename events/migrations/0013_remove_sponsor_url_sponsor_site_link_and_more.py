# Generated by Django 4.2.4 on 2023-08-12 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0012_photoalbum_remove_event_photos_event_photo_album_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sponsor',
            name='url',
        ),
        migrations.AddField(
            model_name='sponsor',
            name='site_link',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='trailer',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='video',
            field=models.URLField(default=2),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Video',
        ),
    ]
