# Generated by Django 3.0.5 on 2020-04-09 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crime_app', '0004_auto_20200409_0611'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='district',
            name='id',
        ),
        migrations.AlterField(
            model_name='district',
            name='Neighborhood',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
    ]
