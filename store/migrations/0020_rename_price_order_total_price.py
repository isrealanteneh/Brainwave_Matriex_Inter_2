# Generated by Django 5.1.1 on 2024-10-01 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0019_alter_order_name"),
    ]

    operations = [
        migrations.RenameField(
            model_name="order",
            old_name="price",
            new_name="total_price",
        ),
    ]
