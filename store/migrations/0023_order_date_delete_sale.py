# Generated by Django 5.1.1 on 2024-10-04 16:19

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0022_alter_product_unit_of_measure"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="date",
            field=models.DateField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name="Sale",
        ),
    ]
