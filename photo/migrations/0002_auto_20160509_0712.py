# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-09 07:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='description',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]