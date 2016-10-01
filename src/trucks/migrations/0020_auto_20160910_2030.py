# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trucks', '0019_auto_20160831_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deleterequest',
            name='truck',
            field=models.CharField(max_length=250),
        ),
    ]
