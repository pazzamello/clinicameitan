# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-12 01:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0003_auto_20160212_0103'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='person',
            name='user',
        ),
        migrations.AlterField(
            model_name='person',
            name='cep',
            field=models.CharField(blank=True, max_length=9),
        ),
        migrations.AddField(
            model_name='patient',
            name='person',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='agenda.Person'),
        ),
        migrations.AddField(
            model_name='patient',
            name='responsible',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='responsible', to='agenda.Person'),
        ),
    ]