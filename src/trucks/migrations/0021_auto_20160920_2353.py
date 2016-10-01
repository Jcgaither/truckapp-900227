# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trucks', '0020_auto_20160910_2030'),
    ]

    operations = [
        migrations.AddField(
            model_name='plustruck',
            name='plus_email',
            field=models.EmailField(max_length=254, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='plustruck',
            name='close_time',
            field=models.CharField(max_length=15, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='plustruck',
            name='open_time',
            field=models.CharField(max_length=15, null=True, blank=True),
        ),
    ]
