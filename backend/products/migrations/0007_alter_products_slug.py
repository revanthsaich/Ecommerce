# Generated by Django 5.1.4 on 2025-01-21 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0006_alter_products_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="products",
            name="slug",
            field=models.SlugField(blank=True, max_length=255),
        ),
    ]
