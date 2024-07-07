# Generated by Django 5.0.6 on 2024-07-06 17:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("doctors", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="speciality",
            name="name",
            field=models.CharField(
                max_length=255,
                unique=True,
                validators=[django.core.validators.RegexValidator("^[a-zA-Z]+$")],
            ),
        ),
    ]