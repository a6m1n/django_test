# Generated by Django 2.2.10 on 2020-02-17 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("manages", "0020_auto_20200217_0727"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sale",
            name="date_end",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="sale",
            name="date_start",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
