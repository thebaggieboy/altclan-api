# Generated by Django 3.2.5 on 2023-12-27 08:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0006_alter_merchandise_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merchandise',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 27, 8, 26, 19, 80328, tzinfo=utc)),
        ),
    ]
