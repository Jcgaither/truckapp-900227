# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trucks', '0017_auto_20160830_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plustruckimage',
            name='food_truck',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, blank=True, to='trucks.PlusTruck', null=True),
        ),
    ]
