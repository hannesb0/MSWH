# Generated by Django 2.1.2 on 2019-03-29 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("system", "0013_configuration_community"),
    ]

    operations = [
        migrations.AddField(
            model_name="community",
            name="size",
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]
