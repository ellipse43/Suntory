# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from rest_framework import mixins, generics, permissions, viewsets
from rest_framework.views import APIView

from .models import Article, ArticleComment, ArticleStory
from .serializers import (
    ArticleSerializer,
    ArticleCommentSerializer,
    ArticleStorySerializer,
    CollectionSerializer,
)


class ArticleViewSet(viewsets.ModelViewSet):

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ArticleCommentViewSet(viewsets.ModelViewSet):

    serializer_class = ArticleCommentSerializer
    permissions_class = (permissions.IsAuthenticatedOrReadOnly, )

    def perform_create(self, serializer):
        id = self.kwargs['id']
        article = get_object_or_404(Article, pk=id)
        serializer.save(article=article, user=self.request.user)

    def get_queryset(self):
        id = self.kwargs['id']
        return ArticleComment.objects.filter(article=id)


class ArticleStoryViewSet(viewsets.ModelViewSet):

    serializer_class = ArticleStorySerializer
    permissions_class = (permissions.IsAuthenticatedOrReadOnly, )
    http_method_names = ['post', ]

    def perform_create(self, serializer):
        id, type_str = self.kwargs['id'], self.kwargs['type_str']
        article = get_object_or_404(Article, pk=id)
        serializer.save(
            article=article,
            user=self.request.user,
            type_id=ArticleStory.TYPES[type_str],
        )

    def get_queryset(self):
        id = self.kwargs['id']
        return ArticleStory.objects.filter(article=id)


class CollectionViewSet(viewsets.ModelViewSet):

    serializer_class = CollectionSerializer
    permissions_class = (permissions.IsAuthenticatedOrReadOnly, )
    http_method_names = ['post', ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
