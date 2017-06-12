from django.contrib import admin

from .models import Post, Profile, Vote

admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Vote)