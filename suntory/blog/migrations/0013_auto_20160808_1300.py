# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-08 13:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20160808_0741'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['-pk']},
        ),
    ]
