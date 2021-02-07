# Generated by Django 3.1.5 on 2021-02-06 17:33

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("KPI", "0005_kpi_month"),
    ]

    operations = [
        migrations.CreateModel(
            name="KPI_quality",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Number", models.TextField(blank=True, null=True)),
                ("employee", models.TextField(blank=True, null=True)),
                ("Assessment", models.IntegerField(default=0)),
                ("quality_сoefficient", models.IntegerField(default=0)),
                ("Total_assessment", models.IntegerField(default=0)),
                ("Total_quality_сoefficient", models.IntegerField(default=0)),
                ("Comments", models.TextField(blank=True, null=True)),
            ],
        ),
    ]