from __future__ import unicode_literals

from django.db import models


class UserManager(models.Manager):
    def validate(self, data):
        error = []
        print "Inside validate"
        if len(data['uname']) <=4:
            print "inside if"
            error.append("Username should have atleast 4 characters and fewer than 10 characters")
            return error
        return error


class People(models.Model):
    first_name = models.CharField(max_length=38, blank=True)
    last_name = models.CharField(max_length= 38, blank=True)
    username = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
