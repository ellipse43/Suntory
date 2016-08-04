# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from rest_framework import routers

from .models import ArticleStory
from .views import (
    ArticleViewSet,
    ArticleCommentViewSet,
    ArticleStoryViewSet,
    CollectionViewSet,
)

router = routers.DefaultRouter()
router.register(r'articles', ArticleViewSet)
router.register(r'articles/(?P<id>[0-9]+)/comments',
                ArticleCommentViewSet, base_name='comments')
router.register(
    r'articles/(?P<id>[0-9]+)/(?P<type_str>({}))'.format(
        '|'.join(ArticleStory.TYPES.keys())),
    ArticleStoryViewSet, base_name='types'
)
router.register(r'collections', CollectionViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
