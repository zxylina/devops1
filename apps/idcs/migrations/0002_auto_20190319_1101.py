# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-19 03:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idcs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idc',
            name='phone',
            field=models.CharField(max_length=15, verbose_name='联系电话'),
        ),
    ]
