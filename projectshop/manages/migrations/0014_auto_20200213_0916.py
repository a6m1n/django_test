# Generated by Django 2.2.10 on 2020-02-13 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("manages", "0013_auto_20200213_0903"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="date_create_order",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="create_date",
            field=models.DateField(blank=True, null=True),
        ),
    ]
