# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-01 20:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Permanents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=200)),
                ('freeRoute', models.BooleanField()),
                ('distance', models.CharField(max_length=200)),
                ('climb', models.CharField(max_length=200)),
                ('permName', models.CharField(max_length=200)),
                ('organizer', models.CharField(max_length=200)),
                ('permLink', models.URLField(null=True)),
            ],
        ),
    ]