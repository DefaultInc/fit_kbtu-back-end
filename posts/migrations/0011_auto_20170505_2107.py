# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-05 15:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_tag_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='color',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='url',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
