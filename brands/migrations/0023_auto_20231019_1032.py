# Generated by Django 3.2.5 on 2023-10-19 09:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0022_auto_20231019_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 19, 9, 32, 22, 421177, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='merchandise',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 19, 9, 32, 22, 421177, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 19, 9, 32, 22, 423299, tzinfo=utc)),
        ),
    ]
