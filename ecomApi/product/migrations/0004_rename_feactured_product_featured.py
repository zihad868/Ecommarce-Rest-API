# Generated by Django 4.2.7 on 2023-12-02 04:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0003_rename_feactured_category_featured"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="feactured",
            new_name="featured",
        ),
    ]