# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trucks', '0007_auto_20160520_0317'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plustruckimage',
            name='truck',
        ),
        migrations.AddField(
            model_name='premiumtrucklocation',
            name='top_truck',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='PlusTruckImage',
        ),
    ]
