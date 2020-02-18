# Generated by Django 2.2.10 on 2020-02-18 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("manages", "0026_auto_20200218_0620"),
    ]

    operations = [
        migrations.RemoveField(model_name="product", name="sale",),
        migrations.AddField(
            model_name="sale",
            name="product",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="manages.Product",
            ),
            preserve_default=False,
        ),
    ]
