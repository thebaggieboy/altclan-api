# Generated by Django 3.2.5 on 2024-07-19 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20240507_2052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviews',
            name='user_email',
        ),
        migrations.AddField(
            model_name='reviews',
            name='brand_name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='reviews',
            name='email',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]
