# Generated by Django 4.2 on 2025-02-11 12:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merchandise',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2025, 2, 11, 12, 23, 18, 883879, tzinfo=datetime.timezone.utc)),
        ),
    ]
