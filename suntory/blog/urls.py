# -*- coding: utf-8 -*-

from django.conf.urls import url

from .views import ArticleList, ArticleDetail, UserList, UserDetail


urlpatterns = [
    url(r'^b/$', ArticleList.as_view()),
    url(r'^b/(?P<pk>[0-9]+)/$', ArticleDetail.as_view()),
    url(r'^u/articles/$', UserList.as_view()),
    url(r'^u/articles/(?P<pk>[0-9]+)/$', UserDetail.as_view()),
]
