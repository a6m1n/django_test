# Generated by Django 2.2.10 on 2020-02-11 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manages', '0004_auto_20200211_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='discount',
            field=models.PositiveIntegerField(unique=True),
        ),
    ]