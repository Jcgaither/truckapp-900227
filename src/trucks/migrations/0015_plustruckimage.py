# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trucks', '0014_feedback_timestamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlusTruckImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.FileField(upload_to=b'images/')),
                ('food_truck', models.ForeignKey(to='trucks.PlusTruck')),
            ],
        ),
    ]
