# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-17 11:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='password',
            field=models.CharField(blank=True, max_length=500, verbose_name='\u4e3b\u673a\u5bc6\u7801'),
        ),
        migrations.AddField(
            model_name='host',
            name='username',
            field=models.CharField(blank=True, max_length=500, verbose_name='\u4e3b\u673a\u7528\u6237\u540d'),
        ),
    ]
