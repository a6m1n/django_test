# Generated by Django 2.2.10 on 2020-02-13 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manages', '0012_auto_20200212_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date_close_order',
            field=models.DateTimeField(default='2020-01-01'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='date_create_order',
            field=models.DateTimeField(default='2020-02-02'),
            preserve_default=False,
        ),
    ]
