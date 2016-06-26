# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions, generics, mixins
from rest_framework.views import APIView
from oauth2_provider.ext.rest_framework import (
    TokenHasReadWriteScope, TokenHasScope)

from .serializers import UserSerializer, GroupSerializer
from .permissions import IsCreationOrIsAuthenticated
from blog.serializers import ArticleSerializer
from blog.models import Article


class UserViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticated,
                          TokenHasReadWriteScope, IsCreationOrIsAuthenticated]
    queryset = User.objects.all()
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
