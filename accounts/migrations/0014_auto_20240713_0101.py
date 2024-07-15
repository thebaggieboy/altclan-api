# Generated by Django 3.2.5 on 2024-07-13 08:01

import datetime
import django.contrib.postgres.fields
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20240624_0529'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='following',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=250, null=True), default=list, size=None),
        ),
        migrations.AlterField(
            model_name='brandprofile',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 13, 8, 0, 59, 745639, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 13, 8, 0, 59, 744638, tzinfo=utc)),
        ),
    ]