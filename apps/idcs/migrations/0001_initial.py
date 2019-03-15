# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-14 03:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Idc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='\u673a\u623f\u540d\u79f0')),
                ('address', models.CharField(max_length=256, verbose_name='\u673a\u623f\u5730\u5740')),
                ('phone', models.CharField(max_length=15, verbose_name='\u8054\u7cfb\u4eba')),
                ('email', models.EmailField(default='null', max_length=254, verbose_name='\u90ae\u4ef6\u5730\u5740')),
                ('letter', models.CharField(max_length=5, verbose_name='IDC\u7b80\u79f0')),
            ],
            options={
                'db_table': 'resources_idc',
            },
        ),
    ]
