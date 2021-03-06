# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-30 10:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0005_auto_20171030_1007'),
    ]

    operations = [
        migrations.AddField(
            model_name='permission',
            name='is_menu',
            field=models.BooleanField(default=False, verbose_name='是否是菜单'),
        ),
        migrations.AlterField(
            model_name='permission',
            name='menu',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='permissions', to='rbac.Menu', verbose_name='所属菜单'),
            preserve_default=False,
        ),
    ]
