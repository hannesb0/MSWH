# Generated by Django 2.1.2 on 2019-02-21 22:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("system", "0005_auto_20190219_1406"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="configuration",
            name="simulation_step",
        ),
        migrations.RemoveField(
            model_name="configuration",
            name="simulation_time",
        ),
    ]
