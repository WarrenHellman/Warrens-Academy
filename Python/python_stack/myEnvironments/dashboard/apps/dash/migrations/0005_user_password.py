# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-02 17:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0004_auto_20180702_0932'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='pass', max_length=50),
            preserve_default=False,
        ),
    ]