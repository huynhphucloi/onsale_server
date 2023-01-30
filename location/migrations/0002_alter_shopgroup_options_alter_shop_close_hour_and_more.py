# Generated by Django 4.1.4 on 2023-01-30 12:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shopgroup',
            options={'verbose_name_plural': 'Shop Groups'},
        ),
        migrations.AlterField(
            model_name='shop',
            name='close_hour',
            field=models.IntegerField(default=20, validators=[django.core.validators.MaxValueValidator(24, message='The latest closing time is 24h'), django.core.validators.MinValueValidator(1, message='Closing time must be at least 1 hour longer than opening time')]),
        ),
        migrations.AlterField(
            model_name='shop',
            name='open_hour',
            field=models.IntegerField(default=8, validators=[django.core.validators.MinValueValidator(0, message='opening time must be between 0h and 23h'), django.core.validators.MaxValueValidator(23, message='opening time must be between 0h and 23h')]),
        ),
    ]