# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trucks', '0002_auto_20160420_0306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='premiumtrucklocation',
            name='plus_postal_code',
            field=models.CharField(default=28117, max_length=100, blank=True),
            preserve_default=False,
        ),
    ]
