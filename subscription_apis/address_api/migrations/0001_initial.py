# Generated by Django 4.1.13 on 2024-09-01 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=120)),
                ('address', models.CharField(blank=True, max_length=120)),
                ('postalcode', models.CharField(blank=True, max_length=20)),
                ('city', models.CharField(blank=True, max_length=120)),
                ('country', models.CharField(blank=True, max_length=80)),
                ('email', models.EmailField(blank=True, max_length=254)),
            ],
        ),
    ]
