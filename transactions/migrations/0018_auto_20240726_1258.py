# Generated by Django 3.2.5 on 2024-07-26 19:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0017_auto_20240719_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 26, 19, 58, 3, 670741, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='tracking_number',
            field=models.CharField(default='bDZ314SLGCOA', max_length=250),
        ),
    ]
