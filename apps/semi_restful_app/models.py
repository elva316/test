from __future__ import unicode_literals

from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX =re.compile('^[A-z]+$')

# Create your models here.
# class user(object):
#     """docstring for ."""
#     def __init__(self, arg):
#         super(, self).__init__()
#         self.arg = arg
class UserManager(models.Manager):
    def validator(self, postData):
        errors = []

            # Check if the email is in db
        if User.objects.filter(email=postData['email']):
            errors.append('Email is already registered')

            # Validate first name
        if len(postData['first_name']) < 2:
            errors.append('First name must be at least 2 characters')
        elif not NAME_REGEX.match(postData['first_name']):
            errors.append('First name must only contain alphabet')

        # Validate last name
        if len(postData['last_name']) < 2:
            errors.append('Last name must be at least 2 characters')
        elif not NAME_REGEX.match(postData['last_name']):
            errors.append('Last name must only contain alphabet')


            # Validate email
        if not EMAIL_REGEX.match(postData['email']):
            errors.append('The email format has to be correct')
        elif User.objects.filter(email=postData['email']):
            errors.append('Email is already registered')

        # if no errors
        # if len(errors) == 0:
        #     # add to database
        #     User.objects.create(first_name=postData['first_name'], last_name=postData['last_name'], email=postData['email'])

        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name  = models.CharField(max_length=255)
    email      = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id) + ' - ' + self.first_name + ' ' + self.last_name + ' - ' + self.email
    objects = UserManager();
