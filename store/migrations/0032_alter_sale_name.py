# Generated by Django 5.1.1 on 2024-10-07 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0031_sale_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sale",
            name="name",
            field=models.CharField(default=None, max_length=100),
        ),
    ]
