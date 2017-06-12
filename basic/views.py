from django.shortcuts import render


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
