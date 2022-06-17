# Generated by Django 3.2 on 2022-06-17 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(blank=True, max_length=30)),
                ('query_type', models.CharField(choices=[('QUOTE', 'Request A Quote'), ('QUERY', 'Ask A Question')], max_length=20)),
                ('description', models.TextField()),
                ('query_date', models.DateField(auto_now_add=True)),
                ('query_image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
