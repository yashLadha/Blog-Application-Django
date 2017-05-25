from django.shortcuts import render, HttpResponse
from django.core.paginator import Paginator, EmptyPage

from .models import Post

def index(request):
    return HttpResponse("Blog Index Page", request)


def all_user_posts(request, user_name):
    """ Sends all posts of particular user """
    user_posts = Post.get_user_post(user_name)
    paginator = Paginator(user_posts, 5)
    page = request.GET.get('page', default=1)
    try:
        user_page_post = paginator.page(page)
    except EmptyPage:
        user_page_post = paginator.page(paginator.num_pages)
    context = {
        'user_all_posts': user_page_post,
    }
    return render(request, 'blog/index.html', context)
