# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import localflavor.us.models
import sorl.thumbnail.fields
import django.contrib.gis.db.models.fields
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trucks', '0008_auto_20160529_0212'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlusTruck',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('plus_truck_name', models.CharField(max_length=200)),
                ('plus_address', models.CharField(max_length=200, blank=True)),
                ('plus_city', models.CharField(max_length=100)),
                ('plus_state', localflavor.us.models.USStateField(max_length=2, choices=[(b'AL', 'Alabama'), (b'AK', 'Alaska'), (b'AS', 'American Samoa'), (b'AZ', 'Arizona'), (b'AR', 'Arkansas'), (b'AA', 'Armed Forces Americas'), (b'AE', 'Armed Forces Europe'), (b'AP', 'Armed Forces Pacific'), (b'CA', 'California'), (b'CO', 'Colorado'), (b'CT', 'Connecticut'), (b'DE', 'Delaware'), (b'DC', 'District of Columbia'), (b'FL', 'Florida'), (b'GA', 'Georgia'), (b'GU', 'Guam'), (b'HI', 'Hawaii'), (b'ID', 'Idaho'), (b'IL', 'Illinois'), (b'IN', 'Indiana'), (b'IA', 'Iowa'), (b'KS', 'Kansas'), (b'KY', 'Kentucky'), (b'LA', 'Louisiana'), (b'ME', 'Maine'), (b'MD', 'Maryland'), (b'MA', 'Massachusetts'), (b'MI', 'Michigan'), (b'MN', 'Minnesota'), (b'MS', 'Mississippi'), (b'MO', 'Missouri'), (b'MT', 'Montana'), (b'NE', 'Nebraska'), (b'NV', 'Nevada'), (b'NH', 'New Hampshire'), (b'NJ', 'New Jersey'), (b'NM', 'New Mexico'), (b'NY', 'New York'), (b'NC', 'North Carolina'), (b'ND', 'North Dakota'), (b'MP', 'Northern Mariana Islands'), (b'OH', 'Ohio'), (b'OK', 'Oklahoma'), (b'OR', 'Oregon'), (b'PA', 'Pennsylvania'), (b'PR', 'Puerto Rico'), (b'RI', 'Rhode Island'), (b'SC', 'South Carolina'), (b'SD', 'South Dakota'), (b'TN', 'Tennessee'), (b'TX', 'Texas'), (b'UT', 'Utah'), (b'VT', 'Vermont'), (b'VI', 'Virgin Islands'), (b'VA', 'Virginia'), (b'WA', 'Washington'), (b'WV', 'West Virginia'), (b'WI', 'Wisconsin'), (b'WY', 'Wyoming')])),
                ('plus_postal_code', models.CharField(max_length=100, blank=True)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326, blank=True)),
                ('plus_description', models.TextField(null=True, blank=True)),
                ('plus_food_type', models.CharField(max_length=45, null=True, blank=True)),
                ('plus_menu', models.TextField(null=True, blank=True)),
                ('plus_menu_photo', models.ImageField(null=True, upload_to=b'images/', blank=True)),
                ('plus_thumbnail', sorl.thumbnail.fields.ImageField(null=True, upload_to=b'images/', blank=True)),
                ('plus_phone_number', localflavor.us.models.PhoneNumberField(max_length=20, null=True, blank=True)),
                ('plus_status', models.CharField(max_length=140, null=True, blank=True)),
                ('slug', models.SlugField()),
                ('top_truck', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_active', models.BooleanField(default=True)),
                ('urllink', models.CharField(max_length=150, blank=True)),
                ('owner', models.ForeignKey(related_name='trucks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameModel(
            old_name='Truck',
            new_name='BaseTruck',
        ),
        migrations.RemoveField(
            model_name='premiumtrucklocation',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='statusupdate',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='statusupdate',
            name='truck',
        ),
        migrations.RemoveField(
            model_name='truckpremium',
            name='owner',
        ),
        migrations.DeleteModel(
            name='PremiumTruckLocation',
        ),
        migrations.DeleteModel(
            name='StatusUpdate',
        ),
        migrations.DeleteModel(
            name='TruckPremium',
        ),
    ]
