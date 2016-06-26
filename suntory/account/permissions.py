# -*- coding: utf-8 -*-

from rest_framework import permissions


class IsCreationOrIsAuthenticated(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated():
            if view.action == 'create':
                return True
            else:
                if request.user.is_superuser:
                    return True
                return False
        return True
