# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-02-16 08:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("metarecord", "0017_remove_record_type"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="function",
            unique_together=set([("function_id", "version"), ("uuid", "version")]),
        ),
    ]
