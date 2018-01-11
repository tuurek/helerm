# Generated by Django 2.0.1 on 2018-01-11 12:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('metarecord', '0034_add_function_classification_related_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='created_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='action_created', to=settings.AUTH_USER_MODEL, verbose_name='created by'),
        ),
        migrations.AlterField(
            model_name='action',
            name='modified_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='action_modified', to=settings.AUTH_USER_MODEL, verbose_name='modified by'),
        ),
        migrations.AlterField(
            model_name='attribute',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='attributes', to='metarecord.AttributeGroup', verbose_name='group'),
        ),
        migrations.AlterField(
            model_name='classification',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='metarecord.Classification', verbose_name='parent'),
        ),
        migrations.AlterField(
            model_name='function',
            name='classification',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='functions', to='metarecord.Classification', verbose_name='classification'),
        ),
        migrations.AlterField(
            model_name='function',
            name='created_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='function_created', to=settings.AUTH_USER_MODEL, verbose_name='created by'),
        ),
        migrations.AlterField(
            model_name='function',
            name='modified_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='function_modified', to=settings.AUTH_USER_MODEL, verbose_name='modified by'),
        ),
        migrations.AlterField(
            model_name='metadataversion',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='modified by'),
        ),
        migrations.AlterField(
            model_name='phase',
            name='created_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='phase_created', to=settings.AUTH_USER_MODEL, verbose_name='created by'),
        ),
        migrations.AlterField(
            model_name='phase',
            name='modified_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='phase_modified', to=settings.AUTH_USER_MODEL, verbose_name='modified by'),
        ),
        migrations.AlterField(
            model_name='record',
            name='created_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='record_created', to=settings.AUTH_USER_MODEL, verbose_name='created by'),
        ),
        migrations.AlterField(
            model_name='record',
            name='modified_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='record_modified', to=settings.AUTH_USER_MODEL, verbose_name='modified by'),
        ),
    ]
