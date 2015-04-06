# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=15)),
                ('surname', models.CharField(max_length=15)),
                ('date_of_birth', models.DateField(null=True, blank=True)),
                ('email', models.EmailField(default=b'example@mail.com', max_length=75)),
                ('phone', models.CharField(max_length=15, blank=True)),
                ('package', models.CharField(blank=True, max_length=8, null=True, choices=[(b'standart', b'Standart'), (b'gold', b'Glod'), (b'platimun', b'Platinum')])),
                ('protect', models.BooleanField(default=False, help_text=b'protection from removal anonymous user')),
                ('courses', models.ManyToManyField(to='courses.Course', null=True, editable=False, blank=True)),
                ('group', models.ManyToManyField(to='courses.Group', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
