# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-27 23:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('style', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='builder.HatStyle')),
            ],
        ),
        migrations.CreateModel(
            name='Jacket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('style', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='builder.JacketStyle')),
            ],
        ),
        migrations.CreateModel(
            name='Shirt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('style', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='builder.ShirtStyle')),
            ],
        ),
    ]