# Generated by Django 3.2.5 on 2024-05-03 12:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20240503_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brandprofile',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 3, 12, 47, 56, 700648, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 3, 12, 47, 56, 700648, tzinfo=utc)),
        ),
    ]
