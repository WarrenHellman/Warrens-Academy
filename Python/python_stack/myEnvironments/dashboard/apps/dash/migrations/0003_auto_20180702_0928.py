# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-02 16:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0002_user_user_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_level',
            field=models.IntegerField(),
        ),
    ]