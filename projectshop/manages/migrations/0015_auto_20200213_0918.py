# Generated by Django 2.2.10 on 2020-02-13 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("manages", "0014_auto_20200213_0916"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="date_close_order",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="product", name="create_date", field=models.DateField(),
        ),
    ]
