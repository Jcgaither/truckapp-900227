# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trucks', '0009_auto_20160601_0246'),
    ]

    operations = [
        migrations.AddField(
            model_name='plustruck',
            name='close_time',
            field=models.TimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='plustruck',
            name='open_time',
            field=models.TimeField(null=True, blank=True),
        ),
    ]
