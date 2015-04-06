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
            name='Coach',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('protect', models.BooleanField(default=False, help_text=b'protection from removal anonymous user')),
                ('name', models.CharField(max_length=15)),
                ('surname', models.CharField(max_length=15)),
                ('email', models.EmailField(default=b'example@gmail.com', max_length=75)),
                ('status', models.CharField(max_length=9, choices=[(b'coach', b'Coach'), (b'assistant', b'Assistant')])),
                ('phone_number', models.CharField(default=b'+38000000000', max_length=15)),
                ('user', models.ForeignKey(default=b'', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
