# Generated by Django 3.2.5 on 2025-01-03 15:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0005_auto_20241217_0528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 3, 15, 52, 29, 605605, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='tracking_number',
            field=models.CharField(default='s91JRW9jp68Q', max_length=250),
        ),
    ]