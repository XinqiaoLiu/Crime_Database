# Generated by Django 3.0.5 on 2020-05-04 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crime_app', '0010_crime_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crime',
            name='Time',
        ),
    ]
