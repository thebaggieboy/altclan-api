# Generated by Django 3.2.5 on 2024-06-24 04:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0011_alter_merchandise_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merchandise',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 24, 4, 29, 18, 688911, tzinfo=utc)),
        ),
    ]
