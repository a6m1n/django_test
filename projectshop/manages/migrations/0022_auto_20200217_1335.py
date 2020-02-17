# Generated by Django 2.2.10 on 2020-02-17 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('manages', '0021_auto_20200217_0729'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sale',
            old_name='date_end',
            new_name='date_create',
        ),
        migrations.RemoveField(
            model_name='sale',
            name='date_start',
        ),
        migrations.AddField(
            model_name='sale',
            name='content_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sale',
            name='object_id',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='product',
            name='sale',
        ),
        migrations.AddField(
            model_name='product',
            name='sale',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='manages.Sale'),
            preserve_default=False,
        ),
    ]