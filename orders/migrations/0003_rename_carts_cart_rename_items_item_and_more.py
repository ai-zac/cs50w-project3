# Generated by Django 4.2 on 2023-05-10 02:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0002_rename_section_items_name"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Carts",
            new_name="Cart",
        ),
        migrations.RenameModel(
            old_name="Items",
            new_name="Item",
        ),
        migrations.RenameModel(
            old_name="ItemsType",
            new_name="ItemType",
        ),
        migrations.RenameModel(
            old_name="Orders",
            new_name="Order",
        ),
        migrations.RenameModel(
            old_name="Users",
            new_name="User",
        ),
    ]
