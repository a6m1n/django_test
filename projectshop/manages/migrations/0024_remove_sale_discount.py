# Generated by Django 2.2.10 on 2020-02-17 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("manages", "0023_auto_20200217_1346"),
    ]

    operations = [
        migrations.RemoveField(model_name="sale", name="discount",),
    ]
