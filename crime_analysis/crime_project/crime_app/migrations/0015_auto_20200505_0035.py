# Generated by Django 3.0.5 on 2020-05-05 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crime_app', '0014_auto_20200504_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='danger',
            name='Type',
            field=models.CharField(max_length=500),
        ),
    ]
