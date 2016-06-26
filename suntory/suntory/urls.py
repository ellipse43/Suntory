# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework')),
    url(r'^oauth/',
        include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^', include('blog.urls')),
    url(r'^', include('account.urls')),
]
