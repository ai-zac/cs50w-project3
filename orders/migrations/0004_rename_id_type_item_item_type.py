# Generated by Django 4.2 on 2023-05-14 22:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0003_rename_carts_cart_rename_items_item_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="item",
            old_name="id_type",
            new_name="item_type",
        ),
    ]