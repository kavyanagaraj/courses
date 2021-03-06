from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Course(models.Model):
    course = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

class Description(models.Model):
    description = models.TextField()
    course_id = models.ForeignKey(Course)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
