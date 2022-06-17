# Generated by Django 3.2 on 2022-06-17 12:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('my_profile', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersprofile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='usersprofile',
            name='phone',
        ),
        migrations.AlterField(
            model_name='usersprofile',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='usersprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userprofile', to='auth.user'),
        ),
    ]
