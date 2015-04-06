# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20150403_0400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='venue',
            field=models.ForeignKey(related_name='course_venue', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='address.Address', null=True),
            preserve_default=True,
        ),
    ]
