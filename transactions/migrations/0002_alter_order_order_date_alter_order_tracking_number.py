# Generated by Django 4.2 on 2025-01-04 23:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 4, 23, 6, 21, 893902, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='tracking_number',
            field=models.CharField(default='JMbd1bYOVfnS', max_length=250),
        ),
    ]
