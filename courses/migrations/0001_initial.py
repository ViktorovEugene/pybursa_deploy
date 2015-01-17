# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


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
                ('name', models.CharField(max_length=225)),
                ('description', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('tecnology', models.CharField(max_length=11, choices=[(b'python', b'Python'), (b'rubby', b'Ruby'), (b'javascript', b'JavaScript')])),
                ('slug', models.SlugField(blank=True)),
                ('assistant', models.ForeignKey(related_name='course_assistant', blank=True, to='coaches.Coach', null=True)),
                ('coach', models.ForeignKey(to='coaches.Coach')),
                ('venue', models.ForeignKey(related_name='course_venue', to='address.Address')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
