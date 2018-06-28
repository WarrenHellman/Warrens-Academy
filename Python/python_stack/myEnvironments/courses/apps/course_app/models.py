# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CourseManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['name'])<6:
            errors['name'] = 'Name must be longer than 5 characters'
        if len(postData['description']) <11:
            errors['description'] = 'Description must be longer than 5 characters'
        return errors

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    objects = CourseManager()