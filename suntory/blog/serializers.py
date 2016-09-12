# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib.auth.models import User
from rest_framework import serializers, validators

from .models import (
    Tag,
    Article,
    ArticleComment,
    ArticleStory,
    Collection,
    CollectionArticle,
    CollectionSubscriber,
)
from account.serializers import UserSerializer


class TagSerializer(serializers.ModelSerializer):

    # 去掉unique检查
    name = serializers.CharField(max_length=50)

    class Meta:
        model = Tag
        fields = ('id', 'name')


class ArticleSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)
    tags = TagSerializer(many=True)

    class Meta:
        model = Article
        fields = ('id', 'user', 'title', 'content', 'created', 'tags', 'pv',
                  'likes_count', 'comments_count', )
        # read_only_fields = ('user', 'tags')

    # 处理多对多关系自定义create&update
    def create(self, validated_data):
        tags = validated_data.pop('tags')
        instance = super(ArticleSerializer, self).create(validated_data)
        for t in tags:
            tag = Tag.objects.filter(name=t['name']).first()
            if tag is None:
                tag = Tag.objects.create(name=t['name'])
            instance.tags.add(tag)
        return instance

    def update(self, instance, validated_data):
        tags = validated_data.pop('tags')
        instance = super(ArticleSerializer, self).update(
            instance, validated_data)
        _tags = []
        for t in tags:
            tag = Tag.objects.filter(name=t['name']).first()
            if tag is None:
                tag = Tag.objects.create(name=t['name'])
            _tags.append(tag)
        if _tags:
            instance.tags.set(_tags)
        return instance


class ArticleCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = ArticleComment
        fields = ('id', 'user', 'reply_user', 'content', 'created')


class ArticleStorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ArticleStory


class CollectionSerializer(serializers.ModelSerializer):

    admins = UserSerializer(many=True, allow_null=True, read_only=True)
    writers = UserSerializer(many=True, allow_null=True, read_only=True)

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
