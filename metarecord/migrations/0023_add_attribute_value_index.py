# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-04-21 09:26
from __future__ import unicode_literals

from django.db import migrations, models


def add_attribute_value_indexes(apps, schema_editor):
    AttributeValue = apps.get_model("metarecord", "AttributeValue")

    for attribute_value in AttributeValue.objects.filter(index=0).order_by(
        "created_at"
    ):
        new_index = (
            max(
                AttributeValue.objects.filter(
                    attribute=attribute_value.attribute
                ).values_list("index", flat=True)
                or [0]
            )
            + 1
        )
        AttributeValue.objects.filter(id=attribute_value.id).update(index=new_index)


class Migration(migrations.Migration):
    dependencies = [
        ("metarecord", "0022_remove_name"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="attributevalue",
            options={
                "ordering": ("index",),
                "verbose_name": "attribute value",
                "verbose_name_plural": "attribute values",
            },
        ),
        migrations.AddField(
            model_name="attributevalue",
            name="index",
            field=models.PositiveSmallIntegerField(db_index=True, default=0),
            preserve_default=False,
        ),
        migrations.RunPython(
            add_attribute_value_indexes, reverse_code=migrations.RunPython.noop
        ),
    ]
