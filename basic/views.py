from django.shortcuts import render, get_object_or_404, HttpResponse
from blog.models import Vote, Post


def index(request):
    """ Index Page of website """
    if request.user.is_authenticated():
        print 'Authenticated user'
        args = {'redirect': 'profile'}
    else:
        print 'User not authenticated'
        args = {'redirect': 'signup'}
    return render(request, 'basic/index.html', args)


def register(request):
    """ Register the User Model """
    return render(request, 'basic/register_form.html')


def upvote(request, id):
    """ Upvotes a given post """
    if request.user:
        post_item = get_object_or_404(Post, pk=id)
        vote = get_object_or_404(Vote, post=post_item)
        vote.up_vote.add(request.user)
        print vote  # for debug purposes only
        return HttpResponse("OK")
    else:
        return HttpResponse("Not OK")


def downvote(request, id):
    """ Downvotes a given post """
    if request.user:
        post_item = get_object_or_404(Post, pk=id)
        vote = get_object_or_404(Vote, post=post_item)
        vote.up_vote.remove(request.user)
        print vote  # for debug purposes only
        return HttpResponse("OK")
    else:
        return HttpResponse("Not OK")
