# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2019-03-05 06:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0053_auto_20190304_1234'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='onsite',
            field=models.BooleanField(default=False),
        ),
    ]