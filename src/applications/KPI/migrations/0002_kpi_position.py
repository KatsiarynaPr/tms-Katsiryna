# Generated by Django 3.1.5 on 2021-01-22 10:40

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("KPI", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="kpi",
            name="position",
            field=models.TextField(blank=True, null=True),
        ),
    ]
