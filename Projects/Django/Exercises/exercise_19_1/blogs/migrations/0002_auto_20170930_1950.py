# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-30 16:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='text',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
