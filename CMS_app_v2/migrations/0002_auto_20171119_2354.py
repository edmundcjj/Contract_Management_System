# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-19 15:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CMS_app_v2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(null=True, upload_to='documents/%Y%m%d/'),
        ),
    ]
