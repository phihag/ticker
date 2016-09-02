# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-27 10:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ticker', '0010_auto_20160827_1031'),
    ]

    operations = [
        # migrations.RemoveField(
        #     model_name='season',
        #     name='leagues',
        # ),
        migrations.AddField(
            model_name='game',
            name='current_set',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='season',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 27, 10, 33, 19, 562396, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='season',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 27, 10, 33, 19, 562396, tzinfo=utc)),
        ),
    ]