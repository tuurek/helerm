# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-02-09 13:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metarecord', '0014_int_id_structural_elements'),
    ]

    operations = [
        migrations.AddField(
            model_name='function',
            name='state',
            field=models.CharField(choices=[('draft', 'Draft'), ('sent_for_review', 'Sent for review'), ('waiting_for_approval', 'Waiting for approval'), ('approved', 'Approved')], default='draft', max_length=20),
        ),
        migrations.AddField(
            model_name='function',
            name='version',
            field=models.PositiveIntegerField(blank=True, db_index=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='function',
            name='function_id',
            field=models.CharField(db_index=True, max_length=16, null=True, verbose_name='function ID'),
        ),
        migrations.AlterUniqueTogether(
            name='function',
            unique_together=set([('function_id', 'version')]),
        ),
    ]