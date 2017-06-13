from django.shortcuts import render, redirect
from blog.models import Post

def show_profile(request):
    """ Show profile of the user """
    if request.user.is_authenticated():
        print 'Authenticated user'
        # TODO : Implement upvote and downvote in post
        user_logged = request.user  # logged in user
        user_posts = Post.get_user_post(user_logged)
        args = {
        	'user': user_logged,
        	'user_posts' : user_posts,
        }

    else:
        print 'User not authenticated'
        return redirect('/login')
    return render(request, 'profile.html', args)
