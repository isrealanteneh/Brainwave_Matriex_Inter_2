# Generated by Django 5.1.1 on 2024-09-29 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0012_delete_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="storeuser",
            name="role",
            field=models.CharField(
                choices=[
                    ("admin", "Admin"),
                    ("manager", "Manager"),
                    ("staff", "Staff"),
                ],
                max_length=100,
            ),
        ),
    ]
