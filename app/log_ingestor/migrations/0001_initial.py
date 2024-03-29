# Generated by Django 4.2.7 on 2023-11-18 07:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LogResource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resource', models.CharField()),
            ],
            options={
                'db_table': 'log_resources',
                'indexes': [models.Index(fields=['resource'], name='log_resourc_resourc_e166f3_idx')],
            },
        ),
        migrations.CreateModel(
            name='LogLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField()),
            ],
            options={
                'db_table': 'log_levels',
                'indexes': [models.Index(fields=['level'], name='log_levels_level_c80459_idx')],
            },
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('timestamp', models.DateTimeField()),
                ('traceId', models.CharField()),
                ('spanId', models.CharField()),
                ('commit', models.CharField()),
                ('metadata', models.JSONField()),
                ('parentResourceId', models.CharField(blank=True, null=True)),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='log_ingestor.loglevel')),
                ('resourceId', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='log_ingestor.logresource')),
            ],
            options={
                'db_table': 'logs',
                'indexes': [models.Index(fields=['timestamp'], name='logs_timesta_e5126f_idx'), models.Index(fields=['level'], name='logs_level_i_0eb69e_idx'), models.Index(fields=['resourceId'], name='logs_resourc_3a4204_idx'), models.Index(fields=['traceId', 'spanId', 'commit'], name='logs_traceId_b68913_idx'), models.Index(fields=['parentResourceId'], name='logs_parentR_272e1c_idx')],
            },
        ),
    ]
