# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from rest_framework import mixins, generics, permissions, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import PermissionDenied, APIException
from guardian.shortcuts import get_perms, get_user_perms

from .permissions import PatchByAdminOrWriterPerm
from .models import (
    Tag,
    Article,
    ArticleComment,
    ArticleStory,
    Collection,
    CollectionArticle,
    CollectionSubscriber,
)
from .serializers import (
    TagSerializer,
    ArticleSerializer,
    ArticleCommentSerializer,
    ArticleStorySerializer,
    CollectionSerializer,
    CollectionArticleSerializer,
    CollectionSubscriberSerializer,
)


class TagViewSet(viewsets.ModelViewSet):

    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )


class ArticleViewSet(viewsets.ModelViewSet):

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        # 嗯，要移走
        instance.pv += 1
        instance.save()
        return Response(serializer.data)

class ArticleCommentViewSet(viewsets.ModelViewSet):

    serializer_class = ArticleCommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def perform_create(self, serializer):
        id = self.kwargs['id']
        article = get_object_or_404(Article, pk=id)
        serializer.save(article=article, user=self.request.user)

    def get_queryset(self):
        id = self.kwargs['id']
        return ArticleComment.objects.filter(article=id)


class ArticleStoryViewSet(viewsets.ModelViewSet):

    serializer_class = ArticleStorySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
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

    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        PatchByAdminOrWriterPerm,
    )
    http_method_names = ['get', 'patch', 'post', ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CollectionArticleViewSet(viewsets.ModelViewSet):

    serializer_class = CollectionArticleSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    http_method_names = ['get', 'post']

    def get_queryset(self):
        id = self.kwargs['id']
        return CollectionArticle.objects.filter(collection=id)


class CollectionSubscriberViewSet(viewsets.ModelViewSet):

    queryset = CollectionSubscriber.objects.all()
    serializer_class = CollectionSubscriberSerializer
    http_method_names = ['post', 'delete']

    def perform_create(self, serializer):
        collection = get_object_or_404(Collection, pk=self.kwargs['id'])
        subscriber = CollectionSubscriber.objects.filter(
            collection=collection, user=self.request.user).first()
        if subscriber:
            raise APIException(detail='已关注')
        serializer.save(user=self.request.user, collection=collection)

    def get_object(self):
        return get_object_or_404(
            CollectionSubscriber,
            collection=self.kwargs['id'],
            user=self.request.user,
        )
