# Generated by Django 4.2 on 2023-05-26 03:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0003_alter_menusection_section_name"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Menu",
            new_name="Item",
        ),
        migrations.RenameModel(
            old_name="MenuSection",
            new_name="ItemSection",
        ),
    ]
