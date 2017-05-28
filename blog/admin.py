from django.contrib import admin

from .models import Post, Register, Profile


admin.site.register(Post)
admin.site.register(Register)
admin.site.register(Profile)
