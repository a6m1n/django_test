# Generated by Django 2.2.10 on 2020-02-11 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manages', '0005_auto_20200211_1344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='status_sale',
        ),
    ]