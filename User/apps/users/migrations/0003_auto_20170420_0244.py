# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-20 02:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_people_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='first_name',
            field=models.CharField(blank=True, max_length=38),
        ),
        migrations.AlterField(
            model_name='people',
            name='last_name',
            field=models.CharField(blank=True, max_length=38),
        ),
    ]
