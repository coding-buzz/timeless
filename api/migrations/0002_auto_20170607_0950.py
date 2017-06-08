# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-07 09:50
from __future__ import unicode_literals

import api.utils
from django.db import migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gallery',
            options={'verbose_name_plural': 'Galleries'},
        ),
        migrations.AlterField(
            model_name='galleryimage',
            name='image',
            field=easy_thumbnails.fields.ThumbnailerImageField(upload_to=api.utils.upload_directory_path),
        ),
    ]
