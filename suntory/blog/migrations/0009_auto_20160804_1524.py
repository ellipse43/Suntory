# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-04 15:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20160804_1438'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='collectionsubscriber',
            unique_together=set([('collection', 'user')]),
        ),
    ]
