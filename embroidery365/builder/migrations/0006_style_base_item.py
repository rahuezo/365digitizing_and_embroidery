# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-27 23:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0005_style'),
    ]

    operations = [
        migrations.AddField(
            model_name='style',
            name='base_item',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='builder.BaseItem'),
            preserve_default=False,
        ),
    ]
