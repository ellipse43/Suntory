# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import mixins, generics, permissions, viewsets
from rest_framework.views import APIView

from .models import Article
from .serializers import ArticleSerializer


class ArticleViewSet(viewsets.ModelViewSet):

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
