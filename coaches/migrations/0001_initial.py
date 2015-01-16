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
                ('name', models.CharField(max_length=225)),
                ('surname', models.CharField(max_length=225)),
                ('email', models.EmailField(default=b'example@gmail.com', max_length=75)),
                ('status', models.CharField(max_length=1, choices=[(b'C', b'Coach'), (b'A', b'Assistant')])),
                ('phone_number', models.CharField(default=b'+38000000000', max_length=15)),
                ('user', models.ForeignKey(default=b'', blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
