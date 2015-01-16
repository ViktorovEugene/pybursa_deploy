# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=225)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=225)),
                ('surname', models.CharField(max_length=225)),
                ('date_of_birth', models.DateField(null=True, blank=True)),
                ('email', models.EmailField(max_length=75)),
                ('phone', models.CharField(max_length=15, blank=True)),
                ('package', models.CharField(default=b'standart', max_length=8, choices=[(b'standart', b'Standart'), (b'gold', b'Glod'), (b'platimun', b'Platinum')])),
                ('courses', models.ManyToManyField(to='courses.Course')),
                ('group', models.ForeignKey(related_name='students', default=b'', to='students.Group')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
