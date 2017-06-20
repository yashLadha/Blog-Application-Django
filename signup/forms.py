from django import forms
from blog.models import Person
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
                'username',
                'password1',
                'password2',
                )


class DateInput(forms.DateInput):
    input_type = 'date'

class MyRegistrationForm(forms.ModelForm):

    birth_date = forms.DateField(widget=DateInput())

    class Meta:
        model = Person
        fields = (
                'birth_date',
                'profile_images',
                )
