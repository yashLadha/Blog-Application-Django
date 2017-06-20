from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^extra/', views.extra_signup, name='extra-sign-up'),
        url(r'^$', views.signup, name='sign-up'),
]
