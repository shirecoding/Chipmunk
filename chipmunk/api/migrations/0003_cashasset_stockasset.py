# Generated by Django 3.1.7 on 2021-03-27 08:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_asset"),
    ]

    operations = [
        migrations.CreateModel(
            name="CashAsset",
            fields=[
                (
                    "asset_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="api.asset",
                    ),
                ),
                ("bank", models.CharField(max_length=100)),
            ],
            bases=("api.asset",),
        ),
        migrations.CreateModel(
            name="StockAsset",
            fields=[
                (
                    "asset_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="api.asset",
                    ),
                ),
                ("shares", models.FloatField(default=0.0)),
                ("share_price", models.FloatField(default=0.0)),
                ("symbol", models.CharField(max_length=100)),
                ("brokerage", models.CharField(max_length=100)),
            ],
            bases=("api.asset",),
        ),
    ]