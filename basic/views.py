from django.shortcuts import render


def index(request):
    """ Index Page of website """
    return render(request, 'basic/index.html')


def register(request):
    """ Register the User Model """
    if request.method == "POST":
        print('Post request received')
    return render(request, 'basic/register_form.html')
