# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-03 12:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ticker', '0013_auto_20160902_1930'),
    ]

    operations = [
        migrations.CreateModel(
            name='ColorDefinition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_hexcode', models.CharField(max_length=32)),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticker.Club')),
            ],
        ),
        migrations.CreateModel(
            name='DefinableColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.AlterField(
            model_name='season',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 3, 12, 15, 10, 945271, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='season',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 3, 12, 15, 10, 945271, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='colordefinition',
            name='color_definition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticker.DefinableColor'),
        ),
        migrations.AlterUniqueTogether(
            name='colordefinition',
            unique_together=set([('club', 'color_definition')]),
        ),
    ]
