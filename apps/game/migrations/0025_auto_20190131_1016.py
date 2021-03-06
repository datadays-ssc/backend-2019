# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2019-01-31 06:46
from __future__ import unicode_literals

import apps.game.models.challenge
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0024_auto_20190131_0607'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamSubmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=apps.game.models.challenge.get_submission_file_directory)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('is_final', models.BooleanField(default=False)),
                ('language', models.CharField(choices=[('cpp', 'C++'), ('java', 'Java'), ('py3', 'Python 3')], default='java', max_length=128)),
                ('status', models.CharField(choices=[('uploading', 'Uploading'), ('uploaded', 'Uploaded'), ('compiling', 'Compiling'), ('compiled', 'Compiled'), ('failed', 'Failed')], default='uploading', max_length=128)),
                ('infra_compile_message', models.CharField(blank=True, max_length=1023, null=True)),
                ('infra_token', models.CharField(blank=True, max_length=256, null=True, unique=True)),
                ('infra_compile_token', models.CharField(blank=True, max_length=256, null=True, unique=True)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to='game.TeamParticipatesChallenge')),
            ],
        ),
        migrations.AddField(
            model_name='instruction',
            name='model_name',
            field=models.CharField(default='Question', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='group_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='instruction',
            name='type',
            field=models.CharField(blank=True, choices=[('multiple_choice', 'multiple_choice'), ('single_answer', 'single_answer'), ('multiple_answer', 'multiple_answer'), ('single_sufficient_answer', 'single_sufficient_answer'), ('single_number', 'single_number'), ('interval_number', 'interval_number'), ('file_upload', 'file_upload')], max_length=200, null=True),
        ),
    ]
