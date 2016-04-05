from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Contact(models.Model):
    class Meta:  # include this to ensure build in IDE
        app_label = "modeltestapp"

    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    mobile = models.CharField(max_length=21)

    def __str__(self):
        return "Yo! it's" + self.first_name
