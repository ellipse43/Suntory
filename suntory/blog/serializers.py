# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib.auth.models import User
from rest_framework import serializers

from .models import (
    Article,
    ArticleComment,
    ArticleStory,
    Collection,
    CollectionArticle,
    CollectionSubscriber,
)
from account.serializers import UserSerializer


class ArticleSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = Article
        fields = ('id', 'user', 'title', 'content', 'created', 'pv',
                  'likes_count', 'comments_count',)
        read_only_fields = ('user', )


class ArticleCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = ArticleComment
        fields = ('id', 'user', 'reply_user', 'content', 'created')


class ArticleStorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ArticleStory


class CollectionSerializer(serializers.ModelSerializer):

    admins = UserSerializer(many=True)
    writers = UserSerializer(many=True)

    class Meta:
        model = Collection
        fields = ('id', 'banner', 'subject', 'description',
                  'created', 'admins', 'writers')


class CollectionArticleSerializer(serializers.ModelSerializer):

    collection = CollectionSerializer()
    article = ArticleSerializer()

    class Meta:
        model = CollectionArticle
        fields = ('id', 'collection', 'article')
        read_only_fields = ('collection', 'article')


class CollectionSubscriberSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source='user.username')
    collection = serializers.ReadOnlyField(source='collection.subject')

    class Meta:
        model = CollectionSubscriber
