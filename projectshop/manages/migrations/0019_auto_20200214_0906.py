# Generated by Django 2.2.10 on 2020-02-14 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manages', '0018_auto_20200214_0746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='start_price',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]
