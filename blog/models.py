from __future__ import unicode_literals

from django.db import models
from django.core.exceptions import ValidationError


class User(models.Model):
    """ Model representation of User
    """

    def __str__(self):
        return str(self.id)


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
    def get_user_post(user):
        """ get all posts of user """
        return Post.objects.filter(author=user).order_by('-date')

    date = models.DateTimeField(auto_now=True)
    tags = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    author = models.OneToOneField(User)
    descriptiom = models.TextField()


class Register(models.Model):
    """ Model representation of Register
    username    : username of the user
    token       : csrf token for the user
    password    : password of the user
    email       : email of the user
    phoneNumber : phoneNumber of the user
    """
    def __str__(self):
        return self.username

    @staticmethod
    def is_user_exists(user_name):
        """ check for exisitng user """
        if Register.objects.filter(username=user_name):
            return False

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not Register.is_user_exists(self.username):
            raise ValidationError('User already exist')
        else:
            super(Register, self).save()

    username = models.CharField(max_length=50)
    token = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=10)
