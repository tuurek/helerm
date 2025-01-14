# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-10-18 13:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("metarecord", "0010_rename_order_to_index"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="recordattachment",
            name="attribute_values",
        ),
        migrations.RemoveField(
            model_name="recordattachment",
            name="created_by",
        ),
        migrations.RemoveField(
            model_name="recordattachment",
            name="modified_by",
        ),
        migrations.RemoveField(
            model_name="recordattachment",
            name="record",
        ),
        migrations.AlterModelOptions(
            name="function",
            options={
                "ordering": ("function_id",),
                "verbose_name": "function",
                "verbose_name_plural": "functions",
            },
        ),
        migrations.AddField(
            model_name="record",
            name="parent",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="children",
                to="metarecord.Record",
                verbose_name="parent",
            ),
        ),
        migrations.DeleteModel(
            name="RecordAttachment",
        ),
    ]
