# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import User, Followee, Follower, Blocker


@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    list_display = ('id', 'username', 'email', 'is_staff',
                    'is_active', 'date_joined', )


@admin.register(Followee)
class FolloweeAdmin(admin.ModelAdmin):

    list_display = ('id', 'user', 'followee', 'created', 'updated', )


@admin.register(Follower)
class FollowerAdmin(admin.ModelAdmin):

    list_display = ('id', 'user', 'follower', 'created', 'updated', )


@admin.register(Blocker)
class BlockerAdmin(admin.ModelAdmin):

    list_display = ('id', 'user', 'blocker', 'created', 'updated', )
