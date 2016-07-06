# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Article, ArticleComment, ArticleStory


class ArticleSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Article
        fields = ('id', 'user', 'title', 'content', 'created', 'pv',
                  'likes_count', 'comments_count',)


class ArticleCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = ArticleComment
        fields = ('id', 'user', 'reply_user', 'content', 'created')


class ArticleStorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ArticleStory
