# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-08 06:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20170608_0637'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='published',
            field=models.BooleanField(default=False),
        ),
    ]
