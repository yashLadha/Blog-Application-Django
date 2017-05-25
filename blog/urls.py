from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<user_name>[\w\s]+)/$', views.all_user_posts, name='user_posts'),
    url(r'^$', views.index, name='index-view'),
]
