# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-26 20:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_authors', '0002_author_notes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='authors',
        ),
        migrations.AddField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(related_name='authors', to='book_authors.Book'),
        ),
    ]
