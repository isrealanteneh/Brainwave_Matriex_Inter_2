# Generated by Django 5.1 on 2024-09-23 16:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Products",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("amount", models.IntegerField()),
                ("unit_price", models.FloatField()),
                ("unit_of_measure", models.CharField(max_length=100)),
                ("date", models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Users",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("password", models.CharField(max_length=100)),
                ("date", models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Sales",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("sold_amount", models.IntegerField()),
                ("date", models.DateField(auto_now_add=True)),
                (
                    "product_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="store.products"
                    ),
                ),
            ],
        ),
    ]
