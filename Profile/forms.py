from django import forms
from pagedown.widgets import PagedownWidget

from blog.models import Post


class PostForm(forms.ModelForm):
    """ Form for the Post creation """
    description = forms.CharField(widget=PagedownWidget())
    class Meta:
        """Meta declaration of Form"""
        model = Post
        fields = [
            'title',
            'description'
        ]
