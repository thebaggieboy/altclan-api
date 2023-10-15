# Generated by Django 3.2.5 on 2023-10-12 15:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0011_auto_20231012_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='merchandise',
            name='discount',
            field=models.CharField(blank=True, default='', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='brand',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 12, 15, 7, 29, 678114, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='merchandise',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 12, 15, 7, 29, 678693, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 12, 15, 7, 29, 680859, tzinfo=utc)),
        ),
    ]
