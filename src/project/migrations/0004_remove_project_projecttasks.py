# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-15 10:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20160415_1057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='projectTasks',
        ),
    ]
