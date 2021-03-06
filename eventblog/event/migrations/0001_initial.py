# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('event_name', models.CharField(max_length=200)),
                ('event_thumbnail', models.ImageField(null=True, upload_to=b'images/', blank=True)),
                ('event_date', models.DateField(verbose_name=b'Event Date')),
                ('event_time', models.DateField(verbose_name=b'Event Time')),
                ('event_location', models.CharField(max_length=400)),
                ('event_description', models.CharField(max_length=700)),
                ('overall_rating', models.FloatField(default=0.0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('feedback_date', models.DateField(auto_now_add=True)),
                ('feedback_time', models.TimeField(auto_now_add=True)),
                ('feedback_data', models.CharField(max_length=700)),
                ('event', models.ForeignKey(to='event.Event')),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('photo', models.ImageField(null=True, upload_to=b'images/event_image/', blank=True)),
                ('event', models.ForeignKey(to='event.Event')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating_date', models.DateField(auto_now_add=True)),
                ('rating_time', models.TimeField(auto_now_add=True)),
                ('rating_star', models.IntegerField(null=True)),
                ('event', models.ForeignKey(to='event.Event')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Suggestion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('suggestion_date', models.DateField(auto_now_add=True)),
                ('suggestion_time', models.TimeField(auto_now_add=True)),
                ('suggestion_data', models.CharField(max_length=700)),
                ('event', models.ForeignKey(to='event.Event')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
