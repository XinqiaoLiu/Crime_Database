# Generated by Django 3.0.5 on 2020-05-06 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crime_app', '0016_auto_20200505_0437'),
    ]

    operations = [
        migrations.RenameField(
            model_name='crime',
            old_name='Time',
            new_name='Ctime',
        ),
    ]
