# Generated by Django 3.2 on 2022-06-12 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_profile', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersprofile',
            name='default_email',
        ),
        migrations.RemoveField(
            model_name='usersprofile',
            name='default_full_name',
        ),
    ]
