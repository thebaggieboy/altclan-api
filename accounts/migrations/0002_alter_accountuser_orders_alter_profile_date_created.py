# Generated by Django 4.2 on 2025-02-11 12:23

import datetime
import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountuser',
            name='orders',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.JSONField(), default=list, size=None),
        ),
        migrations.AlterField(
            model_name='profile',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2025, 2, 11, 12, 23, 18, 893919, tzinfo=datetime.timezone.utc)),
        ),
    ]
