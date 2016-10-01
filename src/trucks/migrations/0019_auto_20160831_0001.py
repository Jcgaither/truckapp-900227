# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trucks', '0018_auto_20160830_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plustruckimage',
            name='food_truck',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='trucks.PlusTruck', null=True),
        ),
    ]
