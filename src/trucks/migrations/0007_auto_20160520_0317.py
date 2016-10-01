# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trucks', '0006_auto_20160517_0221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plustruckimage',
            name='truck',
            field=models.ForeignKey(blank=True, to='trucks.PremiumTruckLocation', null=True),
        ),
    ]
