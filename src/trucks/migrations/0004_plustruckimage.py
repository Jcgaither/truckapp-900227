# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trucks', '0003_auto_20160420_0317'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlusTruckImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'images')),
                ('truck', models.ForeignKey(to='trucks.PremiumTruckLocation')),
            ],
        ),
    ]
