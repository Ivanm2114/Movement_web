# Generated by Django 4.2.4 on 2023-08-09 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_team_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='event',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='events.event'),
            preserve_default=False,
        ),
    ]