# Generated by Django 3.2.5 on 2024-10-11 06:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20240920_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brandprofile',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 11, 6, 48, 29, 349098, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 11, 6, 48, 29, 348092, tzinfo=utc)),
        ),
    ]
