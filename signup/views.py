from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import MyRegistrationForm, UserForm
from django.contrib.auth.models import User
from blog.models import Person


def signup(request):
    """ Sign up view for registration """
    if request.method == 'POST':
        print 'Form submission request received'
        user_form = UserForm(request.POST)
        print user_form.is_valid()
        if user_form.is_valid():
            user = user_form.save()
            print 'User is saved'
            login(request, user)
            return redirect('/signup/extra')
        user_form = UserForm()
        return render(request, 'signup.html', {'user_form': user_form})
    else:
        user_form = UserForm()
    return render(request, 'signup.html', {'user_form': user_form})


def extra_signup(request):
    """ Extra field signup view """
    if request.method == 'POST':
        if request.user.is_authenticated():
            print 'Form submission request received'
            person_form = MyRegistrationForm(request.POST, request.FILES)
            print 'Personal form status: ' + str(person_form.is_valid())
            current_user = request.user
            current_person = Person.objects.get(user=current_user)
            current_person.birth_date = person_form.cleaned_data['birth_date']
            current_person.profile_images = person_form.cleaned_data['profile_images']
            current_person.save()
            print 'Person is updated'
        return redirect('/')
    if request.user.is_authenticated():
        extra_registration = MyRegistrationForm()
        args = {
                'form': extra_registration,
                }
        return render(request, 'extra_signup.html', args)
    return redirect('/')
