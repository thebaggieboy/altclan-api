# Generated by Django 4.2 on 2025-01-11 04:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0003_alter_merchandise_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merchandise',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 11, 4, 14, 16, 805041, tzinfo=datetime.timezone.utc)),
        ),
    ]
