# Generated by Django 4.2.4 on 2023-08-15 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0015_alter_photo_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='trailer',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='video',
            field=models.URLField(blank=True),
        ),
    ]