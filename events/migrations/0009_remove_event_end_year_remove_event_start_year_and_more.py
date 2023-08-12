# Generated by Django 4.2.4 on 2023-08-12 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_head_position'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='end_year',
        ),
        migrations.RemoveField(
            model_name='event',
            name='start_year',
        ),
        migrations.RemoveField(
            model_name='person',
            name='phone',
        ),
        migrations.AddField(
            model_name='event',
            name='partners_event',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='registration_url',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='event',
            name='status',
            field=models.CharField(default='passes', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='photos',
            field=models.ManyToManyField(blank=True, related_name='photos', to='events.photo'),
        ),
        migrations.AlterField(
            model_name='event',
            name='poster',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='poster', to='events.photo'),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='trailer',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='trailer', to='events.video'),
        ),
        migrations.AlterField(
            model_name='event',
            name='video',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='video_report', to='events.video'),
        ),
        migrations.AlterField(
            model_name='head',
            name='photo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='events.photo'),
        ),
        migrations.AlterField(
            model_name='person',
            name='where_knew',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='logo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='events.photo'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]