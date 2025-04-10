# Generated by Django 5.1.1 on 2024-10-04 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0025_remove_order_date_remove_sale_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="catagotires",
            field=models.CharField(
                choices=[
                    ("electronics", "Electronics"),
                    ("clothing", "Clothing"),
                    ("home and kitchen", "Home and Kitchen"),
                    ("beauty and personal care", "Beauty and Personal Care"),
                    ("sports and outdoors", "Sports and Outdoors"),
                    ("groceries", "Groceries"),
                    ("toys and games", "Toys and Games"),
                    ("automotive", "Automotive"),
                    ("books and media", "Books and Media"),
                    ("health and wellness", " Health and Wellness"),
                    ("office supplies", "Office Supplies"),
                    ("pet supplies", "Pet Supplies"),
                    ("automotive", "Automotive"),
                    ("arts and crafts", "Arts and Crafts"),
                    ("baby and kids", "Baby and Kids"),
                ],
                default="pending",
                max_length=100,
            ),
        ),
    ]
