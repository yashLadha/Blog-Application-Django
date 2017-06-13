from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index-view'),
    url(r'^upvote/(?P<ref_name>\d+)/$', views.upvote, name='upvote-post'),
    url(r'^register/', views.register, name='register-view'),
    url(r'^about/$', views.index, name='about-view'),  # Need to implement
]
