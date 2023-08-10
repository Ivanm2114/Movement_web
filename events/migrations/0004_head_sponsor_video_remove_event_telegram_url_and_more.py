# Generated by Django 4.2.4 on 2023-08-10 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_team_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='Head',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='events.person')),
                ('photo', models.ImageField(upload_to='')),
            ],
            bases=('events.person',),
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('logo', models.ImageField(upload_to='')),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='event',
            name='telegram_URL',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='event',
        ),
        migrations.AddField(
            model_name='event',
            name='amount_of_members',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='photos',
            field=models.ManyToManyField(to='events.photo'),
        ),
        migrations.AddField(
            model_name='event',
            name='recent',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='trailer',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='video',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='telegram',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photo',
            name='title',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='member_amt',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
