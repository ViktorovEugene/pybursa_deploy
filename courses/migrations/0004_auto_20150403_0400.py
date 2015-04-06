# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20150403_0359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='venue',
            field=models.ForeignKey(related_name='course_venue', blank=True, to='address.Address', null=True),
            preserve_default=True,
        ),
    ]
