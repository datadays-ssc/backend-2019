# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2019-01-31 15:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0026_auto_20190131_1604'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fileuploadquestion',
            name='download_url',
        ),
        migrations.RemoveField(
            model_name='trial',
            name='dataset_downloaded',
        ),
        migrations.AddField(
            model_name='fileuploadquestion',
            name='dataset_path',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='doc_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='trial',
            name='dataset_link',
            field=models.CharField(blank=True, max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='fileuploadquestion',
            name='answer_file',
            field=models.FileField(null=True, upload_to=models.CharField(blank=True, max_length=200, null=True)),
        ),
        migrations.AlterField(
            model_name='fileuploadquestion',
            name='upload_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]