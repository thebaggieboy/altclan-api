# Generated by Django 3.2.5 on 2023-10-31 07:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 31, 7, 35, 39, 829525, tzinfo=utc)),
        ),
    ]
