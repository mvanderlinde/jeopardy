# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-12 21:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jeopardy', '0003_auto_20170212_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
