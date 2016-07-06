# -*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from oauth2_provider.views import TokenView, RevokeTokenView

from .views import UserViewSet, GroupViewSet, UserArticleList

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

user_list = UserViewSet.as_view({'post': 'create'})


urlpatterns = [
    url(r'', include(router.urls)),
    url(r'users/(?P<user_id>[0-9]+)/articles/$', UserArticleList.as_view()),
    url(r'login/$',  TokenView.as_view()),
    url(r'logout/$', RevokeTokenView.as_view()),
    url(r'signup/$', user_list),
]
