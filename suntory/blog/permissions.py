# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied

from .models import CollectionSubscriber


class PatchByAdminOrWriterPerm(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # 修改需要权限验证
        if request.method in ['PATCH', 'PUT']:
            get_object_or_404(
                CollectionSubscriber,
                user=request.user,
                collection=obj,
            )
            if (request.user.has_perm('admin', obj) is False
                    and request.user.has_perm('writer', obj) is False):
                return False
            return True
        return True
