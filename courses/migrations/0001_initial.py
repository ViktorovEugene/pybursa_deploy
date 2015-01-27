# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
        ('coaches', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('protect', models.BooleanField(default=False, help_text=b'protection from removal anonymous user')),
                ('name', models.CharField(max_length=225)),
                ('description', models.TextField()),
                ('tecnology', models.CharField(default=b'', max_length=11, choices=[(b'python', b'Python'), (b'ruby', b'Ruby'), (b'javascript', b'JavaScript')])),
                ('assistant', models.ForeignKey(related_name='course_assistant', blank=True, to='coaches.Coach', null=True)),
                ('coach', models.ForeignKey(to='coaches.Coach')),
                ('venue', models.ForeignKey(related_name='course_venue', to='address.Address')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, null=True, blank=True)),
                ('protect', models.BooleanField(default=False, help_text=b'protection from removal anonymous user')),
                ('start_date', models.DateField(default=datetime.date(2015, 1, 27))),
                ('end_date', models.DateField(null=True, blank=True)),
                ('number_of_students', models.IntegerField(default=5)),
                ('course', models.ForeignKey(to='courses.Course', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
