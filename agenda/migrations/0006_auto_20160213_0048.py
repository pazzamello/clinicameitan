# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-13 00:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0005_auto_20160213_0022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phone',
            name='person',
        ),
        migrations.AddField(
            model_name='person',
            name='document',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='agenda.Document'),
        ),
        migrations.AddField(
            model_name='person',
            name='phone',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='agenda.Phone'),
        ),
        migrations.AlterField(
            model_name='person',
            name='city',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='district',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='uf',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='document',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='document',
            name='person',
        ),
    ]