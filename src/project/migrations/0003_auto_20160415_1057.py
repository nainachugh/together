# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-15 10:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20160415_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='projectID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Project'),
        ),
    ]
