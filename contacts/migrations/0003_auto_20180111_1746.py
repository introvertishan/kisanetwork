# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-11 12:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20180111_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='Date_created',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
