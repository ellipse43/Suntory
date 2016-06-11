# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Article


class ArticleSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Article
        fields = ('pk', 'user', 'title', 'content', 'created')


class UserSerializer(serializers.ModelSerializer):

    articles = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Article.objects.all())

    class Meta:
        model = User
        fields = ('pk', 'username', 'articles')
