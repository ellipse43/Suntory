# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Article


class ArticleSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Article
        fields = ('id', 'user', 'title', 'content', 'created')
