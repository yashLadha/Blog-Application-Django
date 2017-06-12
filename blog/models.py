from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from taggit.managers import TaggableManager


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


class Vote(models.Model):
    """ Model representation of Vote
    post    : Post for voting
    up_vote : up votes on the post
    """

    def __str__(self):
        return str(self.post) + ":" + self.up_vote

    post = models.OneToOneField(Post, on_delete=models.CASCADE)
    up_vote = models.ManyToManyField(Profile)
