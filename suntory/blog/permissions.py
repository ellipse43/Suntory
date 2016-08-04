# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied

from .models import CollectionSubscriber


class PatchByAdminOrWriterPerm(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        cs = get_object_or_404(
            CollectionSubscriber,
            user=request.user,
            collection=obj,
        )
        if (request.user.has_perm('admin', cs) is False
                and request.user.has_perm('writer', cs) is False):
            return False
        return True
