# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-30 11:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0012_auto_20171030_1135'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Role2Permission',
            new_name='Role2Permission2action',
        ),
    ]
