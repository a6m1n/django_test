# Generated by Django 2.2.10 on 2020-02-12 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("manages", "0011_sale_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="sale",
            name="date_end",
            field=models.DateTimeField(default="2020-01-01"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="sale",
            name="date_start",
            field=models.DateTimeField(default="2020-01-01"),
            preserve_default=False,
        ),
    ]
