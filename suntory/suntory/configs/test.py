# -*- coding: utf-8 -*-

from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'suntory_test',
        'USER': 'root',
        'PASSWORD': 'maomao',
        'HOST': '127.0.0.1',
        'PORT': 3306,
    },
}
