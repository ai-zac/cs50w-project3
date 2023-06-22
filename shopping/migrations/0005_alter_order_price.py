# Generated by Django 4.2.2 on 2023-06-20 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shopping", "0004_alter_platesincart_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="price",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]