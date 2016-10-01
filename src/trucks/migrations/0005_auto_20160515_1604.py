# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trucks', '0004_plustruckimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plustruckimage',
            name='image',
            field=models.ImageField(upload_to=b'attachments'),
        ),
    ]
