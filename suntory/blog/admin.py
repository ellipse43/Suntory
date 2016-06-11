# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Article, ArticleTag


@admin.register(ArticleTag)
class ArticleTagAdmin(admin.ModelAdmin):

    list_display = ('pk', 'code', 'name', 'is_enabled')


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display = ('pk', 'user', 'title', 'created', 'deleted')
