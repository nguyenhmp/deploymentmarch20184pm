# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def validate(self, first_name, last_name):
        if first_name == "":
            print "error"
        if last_name == "":
            print "error"

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    
    def __str__(self):
        return self.first_name + " " + self.last_name

class Shoe(models.Model):
    user = models.ForeignKey(User, related_name="shoes")
    rentals = models.ManyToManyField(User)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.desc + " owned by: " + str(self.user.id)

class Like(models.Model):
    user = models.ForeignKey(User, related_name="likes")
    shoe = models.ForeignKey(Shoe, related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)