# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-07 21:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0013_auto_20171016_1918'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='extra_details',
            field=models.TextField(blank=True),
        ),
    ]
