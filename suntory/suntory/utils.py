# -*- coding: utf-8 -*-

from guardian.shortcuts import get_users_with_perms


def get_users_with_perm(obj, perm):
    data = get_users_with_perms(obj, attach_perms=True)
    r = []
    for user, perms in data.iteritems():
        if perm in perms:
            r.append(user)
    return r
