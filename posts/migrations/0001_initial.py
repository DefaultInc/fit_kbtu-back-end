# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-04 07:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('short_description', models.TextField()),
                ('content', models.TextField()),
                ('publish_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.CharField(max_length=50)),
            ],
        ),
    ]
