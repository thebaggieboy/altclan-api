# Generated by Django 3.2.5 on 2023-10-27 16:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0003_alter_order_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 27, 16, 53, 11, 643221, tzinfo=utc)),
        ),
    ]