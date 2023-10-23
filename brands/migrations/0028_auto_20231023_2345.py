# Generated by Django 3.2.5 on 2023-10-23 22:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0027_auto_20231023_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 23, 22, 45, 9, 176969, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='merchandise',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 23, 22, 45, 9, 178194, tzinfo=utc)),
        ),
    ]
