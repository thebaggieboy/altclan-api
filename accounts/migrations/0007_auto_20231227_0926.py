# Generated by Django 3.2.5 on 2023-12-27 08:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20231227_0923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brandprofile',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 27, 8, 26, 19, 79330, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 27, 8, 26, 19, 79330, tzinfo=utc)),
        ),
    ]
