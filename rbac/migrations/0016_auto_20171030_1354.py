# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-30 13:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0015_permission_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permission',
            name='code',
            field=models.CharField(default=1, max_length=64, unique=True, verbose_name='权限代码'),
            preserve_default=False,
        ),
    ]
