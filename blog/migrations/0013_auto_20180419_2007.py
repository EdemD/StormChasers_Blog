# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-04-20 01:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20180401_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='zipcode',
            field=models.CharField(blank=True, default='', max_length=10),
        ),
    ]