from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from taggit.managers import TaggableManager


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

    def upvote(self):
        """ upvotes a post"""
        vote_obj = get_object_or_404(Vote, post=self)
        print vote_obj

    def up_vote_count(self):
        """returns the upvote for a post"""
        vote_obj = get_object_or_404(Vote, post=self)
        return vote_obj.up_vote.count()

    @staticmethod
    def latest_posts():
        """ retrieves latest post """
        return Post.objects.all().order_by('-date')

    date = models.DateTimeField(auto_now=True)
    tags = TaggableManager()
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    descriptiom = models.TextField()


@receiver(post_save, sender=Post)
def create_vote(sender, instance, **kwargs):
    v = Vote(post=instance)
    v.save()


class Vote(models.Model):
    """ Model representation of Vote
    post    : Post for voting
    up_vote : up votes on the post
    """

    def __str__(self):
        return str(self.post) + " : " + str(self.up_vote.count())

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    up_vote = models.ManyToManyField(User)
