# Generated by Django 4.2.7 on 2023-11-23 16:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.BigIntegerField(default='70000000000', unique=True, validators=[django.core.validators.MinValueValidator(limit_value=10000000000), django.core.validators.MaxValueValidator(limit_value=9999999999)], verbose_name='Номер телефона'),
        ),
    ]
