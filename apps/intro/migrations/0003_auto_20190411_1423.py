# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2019-04-11 09:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('intro', '0002_auto_20190409_0100'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffReborn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('image', models.ImageField(upload_to='staff_pic')),
            ],
        ),
        migrations.CreateModel(
            name='StaffSubTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='StaffTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='staffsubteam',
            name='parent_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='intro.StaffTeam'),
        ),
        migrations.AddField(
            model_name='staffreborn',
            name='sub_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='intro.StaffSubTeam'),
        ),
    ]
