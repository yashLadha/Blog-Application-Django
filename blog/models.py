from __future__ import unicode_literals

from django.db import models
from django.core.exceptions import ValidationError


class Post(models.Model):
    """ Model representation of post
    date        : date of posting the post
    tags        : tag of the post
    title       : title of the post
    author      : author name
    description : main content of the post
    """

    def __str__(self):
        return str(self.id) + " " + self.title + " " + self.author

    @staticmethod
    def get_user_post(user_name):
        """ get all posts of user """
        return Post.objects.filter(author=user_name).order_by('-date')

    date = models.DateTimeField(auto_now=True)
    tags = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    descriptiom = models.TextField()


class Register(models.Model):
    """ Model representation of Register
    username    : username of the user
    password    : password of the user
    email       : email of the user
    phoneNumber : phoneNumber of the user
    """
    def __str__(self):
        return self.username

    @staticmethod
    def is_user_exists():
        """ check for exisitng user """
        if Register.objects.filter(username=self.username):
            return False

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not Register.is_user_exists(self.username):
            raise ValidationError('User already exist')
        else:
            super(Register, self).save(*args, **kwargs)

    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=10)

