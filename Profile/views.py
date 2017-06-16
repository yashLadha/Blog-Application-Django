from django.shortcuts import render, redirect
from blog.models import Post
from .forms import PostForm


def show_profile(request):
    """ Show profile of the user """
    if request.user.is_authenticated():
        print 'Authenticated user'
        user_logged = request.user  # logged in user
        user_posts = Post.get_user_post(user_logged)
        latest_post = Post.latest_posts()
        args = {
            'user': user_logged,
            'user_posts' : user_posts,
            'latest_posts' : latest_post,
        }

    else:
        print 'User not authenticated'
        return redirect('/login')
    return render(request, 'profile.html', args)


def write_post(request):
    """ View for writing posts for user """
    if request.user.is_authenticated():
        if request.method == 'POST':
            print 'Post request received'
            form = PostForm(request.POST)
            if form.is_valid():
                print 'Valid Form received'
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                print 'Post saved'
                #TODO: Add a pop up for more posts to write
        form = PostForm()
        args = {
            'form': form,
        }
        return render(request, 'write_post.html', args)
    return redirect('/login')
