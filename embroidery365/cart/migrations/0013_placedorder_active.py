# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-09 00:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0012_placedorder_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='placedorder',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]