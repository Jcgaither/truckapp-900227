# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('trucks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='premiumtrucklocation',
            name='plus_thumbnail',
            field=sorl.thumbnail.fields.ImageField(null=True, upload_to=b'images/', blank=True),
        ),
    ]
