from django.shortcuts import render
from blog.models import Profile

def index(request):
    """ Index Page of website """
    return render(request, 'basic/index.html')


def register(request):
    """ Register the User Model """
    if request.method == 'GET':
        print('-----Get request received-----')
        user_name = request.GET.get('name_us')
        email = request.GET.get('email_us')
        pass_us = request.GET.get('pass_us')
        conf_pass_us = request.GET.get('conf_pass_us')
        Profile.create_profile(user_name, email, pass_us)
    return render(request, 'basic/register_form.html')
