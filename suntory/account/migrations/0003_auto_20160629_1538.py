# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-29 15:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_blocker_followee_follower'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='blocker',
            unique_together=set([('user', 'blocker')]),
        ),
        migrations.AlterUniqueTogether(
            name='followee',
            unique_together=set([('user', 'followee')]),
        ),
        migrations.AlterUniqueTogether(
            name='follower',
            unique_together=set([('user', 'follower')]),
        ),
    ]