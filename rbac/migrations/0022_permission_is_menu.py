# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-31 04:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0021_auto_20171031_0353'),
    ]

    operations = [
        migrations.AddField(
            model_name='permission',
            name='is_menu',
            field=models.BooleanField(default=False, verbose_name='是否为菜单'),
        ),
    ]
