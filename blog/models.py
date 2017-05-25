from __future__ import unicode_literals

from django.db import models


class Post(models.Model):
    """ Model representation of post
    date        : date of posting the post
    tags        : tag of the post
    title       : title of the post
    author      : author name
    description : main content of the post
    """
    date = models.DateTimeField(auto_now=True)
    tags = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    descriptiom = models.TextField()

    def __str__(self):
        return str(self.id) + " " + self.title + " " + self.author

    @staticmethod
    def get_user_post(user_name):
        """ get all posts of user """
        return Post.objects.filter(author=user_name).order_by('-date')
