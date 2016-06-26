# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from rest_framework import routers

from .views import ArticleViewSet

router = routers.DefaultRouter()
router.register(r'articles', ArticleViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
