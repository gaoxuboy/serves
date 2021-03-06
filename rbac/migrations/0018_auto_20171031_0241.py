# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-31 02:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0017_remove_permission_is_menu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='action',
            name='permission',
        ),
        migrations.AlterUniqueTogether(
            name='role2permission2action',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='role2permission2action',
            name='action',
        ),
        migrations.RemoveField(
            model_name='role2permission2action',
            name='permission',
        ),
        migrations.RemoveField(
            model_name='role2permission2action',
            name='role',
        ),
        migrations.AddField(
            model_name='menu',
            name='is_group',
            field=models.BooleanField(default=False, verbose_name='是否为组'),
        ),
        migrations.AlterField(
            model_name='permission',
            name='url',
            field=models.CharField(max_length=128, verbose_name='URL'),
        ),
        migrations.DeleteModel(
            name='Action',
        ),
        migrations.DeleteModel(
            name='Role2Permission2action',
        ),
    ]
