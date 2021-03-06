# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-22 10:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ticker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='FieldAllocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('end_allocation', models.DateTimeField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticker.Field')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticker.Game')),
            ],
        ),
        migrations.AddField(
            model_name='point',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 22, 10, 14, 36, 280166, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='club',
            name='fields',
            field=models.ManyToManyField(to='ticker.Field'),
        ),
        migrations.AddField(
            model_name='team',
            name='fields',
            field=models.ManyToManyField(to='ticker.Field'),
        ),
    ]
