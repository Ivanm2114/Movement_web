# Generated by Django 4.2.4 on 2023-08-10 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_head_sponsor_video_remove_event_telegram_url_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='end_year',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='start_year',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
