# Generated by Django 4.2 on 2025-01-11 05:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0004_alter_order_order_date_alter_order_tracking_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 11, 5, 11, 13, 657966, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='tracking_number',
            field=models.CharField(default='BQ6wguDIvEc9', max_length=250),
        ),
    ]
