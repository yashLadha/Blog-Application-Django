from __future__ import unicode_literals
from taggit.managers import TaggableManager

from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class Profile(models.Model):
    """ Model representation of User
    user        : Default User module
    birth_date  : birth date of the user
    description : description about themselves
    """

    def __str__(self):
        return str(self.user)

    @staticmethod
    def create_profile(user_name, email, password):
        """ Create user profile object """
        user = User.objects.create_user(user_name, email, password)
        user.save()

    user = models.OneToOneField(User, on_delete=models.CASCADE)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """ Creates a custom user """
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """ Saves a custom user """
    instance.profile.save()


class Post(models.Model):
    """ Model representation of post
    date        : date of posting the post
    tags        : tag's of the post
    title       : title of the post
    author      : author name
    description : main content of the post
    """

    def __str__(self):
        return str(self.id) + " " + self.title + " " + str(self.author)

    @staticmethod
    def get_user_post(user):
        """ get all posts of user """
        return Post.objects.filter(author=user).order_by('-date')

    date = models.DateTimeField(auto_now=True)
    tags = TaggableManager()
    title = models.CharField(max_length=100)
    author = models.OneToOneField(Profile, on_delete=models.CASCADE)
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


class Vote(models.Model):
    """ Model representation of Vote
    post    : Post for voting
    up_vote : up votes on the post
    """

    def __str__(self):
        return str(self.post) + ":" + self.up_vote

    post = models.OneToOneField(Post, on_delete=models.CASCADE)
    up_vote = models.ManyToManyField(Profile)
