# Generated by Django 4.2 on 2025-01-10 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('brand_name', models.CharField(blank=True, max_length=250, null=True)),
                ('slug', models.SlugField()),
                ('review', models.TextField(blank=True, default='', null=True)),
            ],
        ),
    ]
