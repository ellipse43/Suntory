from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class ArticleTag(models.Model):

    is_enabled = models.BooleanField(default=True)
    code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name


class Article(models.Model):

    user = models.ForeignKey(
        User, related_name='articles',
        on_delete=models.SET_NULL, blank=True, null=True)
    tags = models.ManyToManyField(ArticleTag)
    title = models.CharField(max_length=128, blank=True, default='')
    content = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ('-pk', )

    def __unicode__(self):
        return self.title or self.content[:20]
