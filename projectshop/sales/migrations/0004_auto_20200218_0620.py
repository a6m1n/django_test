# Generated by Django 2.2.10 on 2020-02-18 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("sales", "0003_auto_20200217_1433"),
    ]

    operations = [
        migrations.RemoveField(model_name="alltimediscount",
                               name="content_type",),
        migrations.RemoveField(model_name="alltimediscount",
                               name="object_id",),
        migrations.RemoveField(model_name="promocodediscount",
                               name="content_type",),
        migrations.RemoveField(model_name="promocodediscount",
                               name="object_id",),
        migrations.RemoveField(model_name="storagediscount",
                               name="content_type",),
        migrations.RemoveField(model_name="storagediscount",
                               name="object_id",),
        migrations.RemoveField(model_name="temporarydiscount",
                               name="content_type",),
        migrations.RemoveField(model_name="temporarydiscount",
                               name="object_id",),
    ]