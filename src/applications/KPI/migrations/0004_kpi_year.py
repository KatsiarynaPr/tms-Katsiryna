# Generated by Django 3.1.5 on 2021-02-06 16:35

import django.core.validators
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("KPI", "0003_kpi_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="kpi",
            name="year",
            field=models.PositiveIntegerField(
                default=2021,
                help_text="Use the following format: <YYYY>",
                validators=[
                    django.core.validators.MinValueValidator(2020),
                    django.core.validators.MaxValueValidator(2045),
                ],
            ),
            preserve_default=False,
        ),
    ]