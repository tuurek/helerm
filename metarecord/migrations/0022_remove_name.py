# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-04-11 19:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("metarecord", "0021_add_validation_dates"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="action",
            name="name",
        ),
        migrations.RemoveField(
            model_name="phase",
            name="name",
        ),
        migrations.RemoveField(
            model_name="record",
            name="name",
        ),
    ]
