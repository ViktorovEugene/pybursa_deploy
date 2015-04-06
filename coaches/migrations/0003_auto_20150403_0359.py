# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0002_auto_20150403_0042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coach',
            name='name',
            field=models.CharField(max_length=15),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coach',
            name='surname',
            field=models.CharField(max_length=15),
            preserve_default=True,
        ),
    ]
