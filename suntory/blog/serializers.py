# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib.auth.models import User
from rest_framework import serializers

from .models import (
    Article,
    ArticleComment,
    ArticleStory,
    Collection,
    CollectionSubscriber,
)


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


class CollectionSerializer(serializers.ModelSerializer):

    # author = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Collection
        fields = ('id', 'banner', 'subject', 'description', 'created')


class CollectionSubscriberSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source='user.username')
    collection = serializers.ReadOnlyField(source='collection.subject')

    class Meta:
        model = CollectionSubscriber
