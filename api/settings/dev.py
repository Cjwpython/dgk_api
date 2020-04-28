#coding: utf-8
from .base import *

DEBUG = True
ENV = 'development'

INSTALLED_APPS += [
    'drf_generators',
    'autofixture',
    'drf_yasg'
]

#数据库配置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dgk',  # 数据库名称
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'mysql',
    }
}


CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis:6379/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}