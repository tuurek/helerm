# Generated by Django 2.2.16 on 2020-10-02 11:27

from django.db import migrations


def set_existing_classifications_as_approved(apps, schema_editor):
    Classification = apps.get_model("metarecord", "Classification")
    Classification.objects.all().update(state="approved")


class Migration(migrations.Migration):
    dependencies = [
        ("metarecord", "0046_classification_versioning"),
    ]

    operations = [
        migrations.RunPython(
            set_existing_classifications_as_approved, migrations.RunPython.noop
        )
    ]
