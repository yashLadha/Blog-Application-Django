from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.show_profile, name='show-profile'),
    url(r'^write/', views.write_post, name='write-posts'),
]
