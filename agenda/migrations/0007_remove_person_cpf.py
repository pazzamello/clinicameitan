# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-13 01:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0006_auto_20160213_0048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='cpf',
        ),
    ]
