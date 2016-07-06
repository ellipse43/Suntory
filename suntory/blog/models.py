# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.utils.functional import cached_property


class ArticleTag(models.Model):

    is_enabled = models.BooleanField(default=True)
    code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name


class Article(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='articles',
        on_delete=models.SET_NULL, blank=True, null=True)
    tags = models.ManyToManyField(ArticleTag)
    title = models.CharField(max_length=128, blank=True, default='')
    content = models.TextField()
    pv = models.IntegerField(default=0)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ('-pk', )

    def __unicode__(self):
        return self.title or self.content[:20]

    @cached_property
    def likes_count(self):
        return ArticleStory.objects.filter(
            article=self,
            user=self.user,
            type_id=ArticleStory.TYPE_LIKE,
        ).count()

    @cached_property
    def comments_count(self):
        return self.comments.count()


class ArticleComment(models.Model):

    article = models.ForeignKey(
        Article, related_name='comments',
        on_delete=models.SET_NULL, blank=True, null=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='comments', on_delete=models.SET_NULL,
        blank=True, null=True)
    reply_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
        blank=True, null=True)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)

    def __unicode__(self):
        return self.content


class ArticleStory(models.Model):
    '''
    用故事来代表每朵花纹，师姐说的。。。
    '''

    TYPE_NULL = 0
    TYPE_THUMB_UP = 1
    TYPE_THUMB_DOWN = 2
    TYPE_LIKE = 3
    TYPE_COLLECT = 4

    TYPES = {
        'null': TYPE_NULL,
        'thumb_up': TYPE_THUMB_UP,
        'thumb_down': TYPE_THUMB_DOWN,
        'like': TYPE_LIKE,
        'collect': TYPE_COLLECT,
    }

    article = models.ForeignKey(
        Article,
        on_delete=models.SET_NULL, blank=True, null=True)
    type_id = models.IntegerField(default=TYPE_NULL)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
        blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.article
