# Generated by Django 5.0.6 on 2024-06-09 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_alter_profile_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='email',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
    ]
