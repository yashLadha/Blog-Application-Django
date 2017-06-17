from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.views.static import serve


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^profile/', include('Profile.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^signup/', include('signup.urls')),
    url(r'^login/', auth_views.login, name='login'),
    url(r'^logout/', auth_views.logout, name='log-out'),
    url(r'^', include('basic.urls')),
    url(r'^static/(?P<path>.*)$', serve, { 'document_root': settings.STATIC_ROOT  }),
]
