# Generated by Django 3.2.5 on 2023-10-23 22:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_alter_brandprofile_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brandprofile',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 23, 22, 45, 9, 184973, tzinfo=utc)),
        ),
    ]