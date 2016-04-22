# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-22 13:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('metarecord', '0005_freetext_attributes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='time of creation')),
                ('modified_at', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='time of modification')),
                ('name', models.CharField(max_length=256, verbose_name='name')),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attribute_created', to=settings.AUTH_USER_MODEL, verbose_name='created by')),
                ('modified_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attribute_modified', to=settings.AUTH_USER_MODEL, verbose_name='modified by')),
                ('identifier', models.CharField(verbose_name='identifier', max_length=64, unique=True, db_index=True)),
            ],
            options={
                'verbose_name_plural': 'attributes',
                'verbose_name': 'attribute',
            },
        ),
        migrations.CreateModel(
            name='AttributeValue',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='time of creation')),
                ('modified_at', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='time of modification')),
                ('value', models.CharField(max_length=256, verbose_name='value')),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='values', to='metarecord.Attribute', verbose_name='attribute')),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attributevalue_created', to=settings.AUTH_USER_MODEL, verbose_name='created by')),
                ('modified_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attributevalue_modified', to=settings.AUTH_USER_MODEL, verbose_name='modified by')),
            ],
            options={
                'verbose_name_plural': 'attribute values',
                'verbose_name': 'attribute value',
            },
        ),
        migrations.RemoveField(
            model_name='informationsystem',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='informationsystem',
            name='modified_by',
        ),
        migrations.RemoveField(
            model_name='paperrecordarchiveretentionperiod',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='paperrecordarchiveretentionperiod',
            name='modified_by',
        ),
        migrations.RemoveField(
            model_name='paperrecordretentionorder',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='paperrecordretentionorder',
            name='modified_by',
        ),
        migrations.RemoveField(
            model_name='paperrecordworkplaceretentionperiod',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='paperrecordworkplaceretentionperiod',
            name='modified_by',
        ),
        migrations.RemoveField(
            model_name='personaldata',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='personaldata',
            name='modified_by',
        ),
        migrations.RemoveField(
            model_name='protectionclass',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='protectionclass',
            name='modified_by',
        ),
        migrations.RemoveField(
            model_name='publicityclass',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='publicityclass',
            name='modified_by',
        ),
        migrations.RemoveField(
            model_name='retentioncalculationbasis',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='retentioncalculationbasis',
            name='modified_by',
        ),
        migrations.RemoveField(
            model_name='retentionperiod',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='retentionperiod',
            name='modified_by',
        ),
        migrations.RemoveField(
            model_name='retentionreason',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='retentionreason',
            name='modified_by',
        ),
        migrations.RemoveField(
            model_name='securityperiod',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='securityperiod',
            name='modified_by',
        ),
        migrations.RemoveField(
            model_name='securityperiodcalculationbasis',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='securityperiodcalculationbasis',
            name='modified_by',
        ),
        migrations.RemoveField(
            model_name='securityreason',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='securityreason',
            name='modified_by',
        ),
        migrations.RemoveField(
            model_name='socialsecuritynumber',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='socialsecuritynumber',
            name='modified_by',
        ),
        migrations.RemoveField(
            model_name='action',
            name='additional_information',
        ),
        migrations.RemoveField(
            model_name='action',
            name='information_system',
        ),
        migrations.RemoveField(
            model_name='action',
            name='personal_data',
        ),
        migrations.RemoveField(
            model_name='action',
            name='protection_class',
        ),
        migrations.RemoveField(
            model_name='action',
            name='publicity_class',
        ),
        migrations.RemoveField(
            model_name='action',
            name='retention_calculation_basis',
        ),
        migrations.RemoveField(
            model_name='action',
            name='retention_period',
        ),
        migrations.RemoveField(
            model_name='action',
            name='retention_reason',
        ),
        migrations.RemoveField(
            model_name='action',
            name='security_period',
        ),
        migrations.RemoveField(
            model_name='action',
            name='security_period_calculation_basis',
        ),
        migrations.RemoveField(
            model_name='action',
            name='security_reason',
        ),
        migrations.RemoveField(
            model_name='action',
            name='social_security_number',
        ),
        migrations.RemoveField(
            model_name='function',
            name='additional_information',
        ),
        migrations.RemoveField(
            model_name='function',
            name='information_system',
        ),
        migrations.RemoveField(
            model_name='function',
            name='personal_data',
        ),
        migrations.RemoveField(
            model_name='function',
            name='protection_class',
        ),
        migrations.RemoveField(
            model_name='function',
            name='publicity_class',
        ),
        migrations.RemoveField(
            model_name='function',
            name='retention_calculation_basis',
        ),
        migrations.RemoveField(
            model_name='function',
            name='retention_period',
        ),
        migrations.RemoveField(
            model_name='function',
            name='retention_reason',
        ),
        migrations.RemoveField(
            model_name='function',
            name='security_period',
        ),
        migrations.RemoveField(
            model_name='function',
            name='security_period_calculation_basis',
        ),
        migrations.RemoveField(
            model_name='function',
            name='security_reason',
        ),
        migrations.RemoveField(
            model_name='function',
            name='social_security_number',
        ),
        migrations.RemoveField(
            model_name='phase',
            name='additional_information',
        ),
        migrations.RemoveField(
            model_name='phase',
            name='information_system',
        ),
        migrations.RemoveField(
            model_name='phase',
            name='personal_data',
        ),
        migrations.RemoveField(
            model_name='phase',
            name='protection_class',
        ),
        migrations.RemoveField(
            model_name='phase',
            name='publicity_class',
        ),
        migrations.RemoveField(
            model_name='phase',
            name='retention_calculation_basis',
        ),
        migrations.RemoveField(
            model_name='phase',
            name='retention_period',
        ),
        migrations.RemoveField(
            model_name='phase',
            name='retention_reason',
        ),
        migrations.RemoveField(
            model_name='phase',
            name='security_period',
        ),
        migrations.RemoveField(
            model_name='phase',
            name='security_period_calculation_basis',
        ),
        migrations.RemoveField(
            model_name='phase',
            name='security_reason',
        ),
        migrations.RemoveField(
            model_name='phase',
            name='social_security_number',
        ),
        migrations.RemoveField(
            model_name='record',
            name='additional_information',
        ),
        migrations.RemoveField(
            model_name='record',
            name='information_system',
        ),
        migrations.RemoveField(
            model_name='record',
            name='paper_record_archive_retention_period',
        ),
        migrations.RemoveField(
            model_name='record',
            name='paper_record_retention_location',
        ),
        migrations.RemoveField(
            model_name='record',
            name='paper_record_retention_order',
        ),
        migrations.RemoveField(
            model_name='record',
            name='paper_record_retention_responsible_person',
        ),
        migrations.RemoveField(
            model_name='record',
            name='paper_record_workplace_retention_period',
        ),
        migrations.RemoveField(
            model_name='record',
            name='personal_data',
        ),
        migrations.RemoveField(
            model_name='record',
            name='protection_class',
        ),
        migrations.RemoveField(
            model_name='record',
            name='publicity_class',
        ),
        migrations.RemoveField(
            model_name='record',
            name='retention_calculation_basis',
        ),
        migrations.RemoveField(
            model_name='record',
            name='retention_period',
        ),
        migrations.RemoveField(
            model_name='record',
            name='retention_reason',
        ),
        migrations.RemoveField(
            model_name='record',
            name='security_period',
        ),
        migrations.RemoveField(
            model_name='record',
            name='security_period_calculation_basis',
        ),
        migrations.RemoveField(
            model_name='record',
            name='security_reason',
        ),
        migrations.RemoveField(
            model_name='record',
            name='social_security_number',
        ),
        migrations.AlterField(
            model_name='recordtype',
            name='value',
            field=models.CharField(max_length=256, verbose_name='name'),
        ),
        migrations.DeleteModel(
            name='InformationSystem',
        ),
        migrations.DeleteModel(
            name='PaperRecordArchiveRetentionPeriod',
        ),
        migrations.DeleteModel(
            name='PaperRecordRetentionOrder',
        ),
        migrations.DeleteModel(
            name='PaperRecordWorkplaceRetentionPeriod',
        ),
        migrations.DeleteModel(
            name='PersonalData',
        ),
        migrations.DeleteModel(
            name='ProtectionClass',
        ),
        migrations.DeleteModel(
            name='PublicityClass',
        ),
        migrations.DeleteModel(
            name='RetentionCalculationBasis',
        ),
        migrations.DeleteModel(
            name='RetentionPeriod',
        ),
        migrations.DeleteModel(
            name='RetentionReason',
        ),
        migrations.DeleteModel(
            name='SecurityPeriod',
        ),
        migrations.DeleteModel(
            name='SecurityPeriodCalculationBasis',
        ),
        migrations.DeleteModel(
            name='SecurityReason',
        ),
        migrations.DeleteModel(
            name='SocialSecurityNumber',
        ),
        migrations.AddField(
            model_name='action',
            name='attribute_values',
            field=models.ManyToManyField(to='metarecord.AttributeValue', verbose_name='attribute values'),
        ),
        migrations.AddField(
            model_name='function',
            name='attribute_values',
            field=models.ManyToManyField(to='metarecord.AttributeValue', verbose_name='attribute values'),
        ),
        migrations.AddField(
            model_name='phase',
            name='attribute_values',
            field=models.ManyToManyField(to='metarecord.AttributeValue', verbose_name='attribute values'),
        ),
        migrations.AddField(
            model_name='record',
            name='attribute_values',
            field=models.ManyToManyField(to='metarecord.AttributeValue', verbose_name='attribute values'),
        ),
    ]