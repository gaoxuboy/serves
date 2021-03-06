# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-30 10:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0008_remove_action_type_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='PermissionCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=32, verbose_name='标题')),
                ('code', models.CharField(max_length=16, verbose_name='代码')),
            ],
        ),
        migrations.AddField(
            model_name='permission',
            name='code',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='rbac.PermissionCode', verbose_name='权限代码'),
            preserve_default=False,
        ),
    ]
