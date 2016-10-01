# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trucks', '0005_auto_20160515_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plustruckimage',
            name='image',
            field=models.ImageField(null=True, upload_to=b'attachments', blank=True),
        ),
    ]
