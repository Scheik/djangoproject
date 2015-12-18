# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-18 20:00
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=40)),
                ('title', models.CharField(max_length=200)),
                ('bodytext', tinymce.models.HTMLField()),
                ('timestamp', models.DateTimeField()),
            ],
        ),
    ]
