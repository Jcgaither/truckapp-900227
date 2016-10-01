# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trucks', '0021_auto_20160920_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plustruck',
            name='plus_status',
            field=models.CharField(default=b'', max_length=140, null=True, blank=True),
        ),
    ]
