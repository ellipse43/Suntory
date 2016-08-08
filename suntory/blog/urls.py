# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from rest_framework import routers

from .models import ArticleStory
from .views import (
    TagViewSet,
    ArticleViewSet,
    ArticleCommentViewSet,
    ArticleStoryViewSet,
    CollectionViewSet,
    CollectionArticleViewSet,
    CollectionSubscriberViewSet,
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
router.register(r'tags', TagViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'collections/(?P<id>[0-9]+)/articles',
        CollectionArticleViewSet.as_view({
            'get': 'list',
            'post': 'create',
        })),
    url(r'collections/(?P<id>[0-9]+)/subscribe',
        CollectionSubscriberViewSet.as_view({'post': 'create'}),
        name='collection_subscribe'),
    url(r'collections/(?P<id>[0-9]+)/unsubscribe',
        CollectionSubscriberViewSet.as_view({'delete': 'destroy'}),
        name='collection_unsubscribe'),
]
