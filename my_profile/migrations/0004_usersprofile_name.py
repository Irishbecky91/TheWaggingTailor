# Generated by Django 3.2 on 2022-06-17 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_profile', '0003_remove_usersprofile_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersprofile',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
