# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-04 01:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20160707_1512'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='collectionsubscriber',
            options={'ordering': ('-pk',), 'permissions': (('admin', '\u7ba1\u7406\u5458'), ('writer', '\u534f\u4f5c\u8005'), ('audience', '\u56f4\u89c2\u7fa4\u4f17'))},
        ),
    ]
