from __future__ import unicode_literals

from django.db import models


class Post(models.Model):
    """ Model representation of post
    initDate    : initialization Date
    tags        : tag of the post
    title       : title of the post
    description : main content of the post
    """
    initDate = models.DateTimeField()
    tags = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    descriptiom = models.TextField()

    def __str__(self):
        return str(self.id) + " " + self.title
