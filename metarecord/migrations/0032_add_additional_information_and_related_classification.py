# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-21 13:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("metarecord", "0031_add_deleted_state"),
    ]

    operations = [
        migrations.AddField(
            model_name="classification",
            name="additional_information",
            field=models.TextField(blank=True, verbose_name="additional information"),
        ),
        migrations.AddField(
            model_name="classification",
            name="related_classification",
            field=models.TextField(blank=True, verbose_name="related classification"),
        ),
    ]
