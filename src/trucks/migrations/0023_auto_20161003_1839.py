# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trucks', '0022_auto_20161001_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plustruck',
            name='close_time',
            field=models.CharField(default=b'', max_length=15, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='plustruck',
            name='open_time',
            field=models.CharField(default=b'', max_length=15, null=True, blank=True),
        ),
    ]
