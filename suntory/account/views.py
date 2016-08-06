# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import json

from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework import viewsets, permissions, generics, mixins
from rest_framework.views import APIView
from oauth2_provider.ext.rest_framework import (
    TokenHasReadWriteScope, TokenHasScope)
from oauth2_provider.views import TokenView as BaseTokenView
from oauth2_provider.models import AccessToken

from .serializers import UserSerializer, GroupSerializer
from .permissions import IsCreationOrIsAuthenticated
from blog.serializers import ArticleSerializer, CollectionSerializer
from blog.models import Article, Collection


class UserViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticated,
                          TokenHasReadWriteScope, IsCreationOrIsAuthenticated]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = (permissions.AllowAny,)
        return super(UserViewSet, self).get_permissions()


class GroupViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['groups']
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class UserArticleList(generics.ListAPIView):

    serializer_class = ArticleSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Article.objects.filter(user_id=user_id)


class UserCollectionList(generics.ListAPIView):

    serializer_class = CollectionSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Collection.objects.filter(author_id=user_id)


class TokenView(BaseTokenView):

    def post(self, request, *args, **kwargs):
        response = super(TokenView, self).post(request, *args, **kwargs)

        # 自己APP才使用
        body = json.loads(response.content)
        token = AccessToken.objects.filter(
            token=body.get('access_token')).last()
        if token:
            response.content = json.dumps(
                dict(
                    body,
                    user={
                        'id': token.user.id,
                        'username': token.user.username,
                    }
                )
            )
        return response
