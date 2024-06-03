# Generated by Django 5.0.6 on 2024-06-03 17:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_profile_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='balance',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]