# Generated by Django 3.1.7 on 2021-03-27 08:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0003_cashasset_stockasset"),
    ]

    operations = [
        migrations.CreateModel(
            name="Share",
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
                ("name", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=100)),
                ("price", models.FloatField(default=0.0)),
                (
                    "unit",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.share"
                    ),
                ),
            ],
        ),
    ]
