# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coach',
            name='status',
            field=models.CharField(max_length=9, choices=[(b'coach', b'Coach'), (b'assistatn', b'Assistant')]),
            preserve_default=True,
        ),
    ]
