# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-30 09:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0002_auto_20171030_0901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='code',
            field=models.CharField(max_length=64, verbose_name='代码'),
        ),
        migrations.AlterField(
            model_name='action',
            name='type_id',
            field=models.SmallIntegerField(choices=[(1, 'Url'), (2, 'Action')], default=1),
        ),
    ]
