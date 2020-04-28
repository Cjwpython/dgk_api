# coding: utf-8
from .settings import *
import pymysql

pymysql.install_as_MySQLdb()

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
                     "simpleui",
                     "user.apps.UserConfig",
                     "rest_framework",
                    "rest_framework.authtoken",
                 ] + INSTALLED_APPS

MIDDLEWARE += [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',  # 注意顺序
]

# 时间配置

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

AUTH_USER_MODEL = "user.User"

# rest 配置
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
    'PAGE_SIZE': 10,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DATETIME_FORMAT': "%Y-%m-%d %H:%M:%S",
    'COERCE_DECIMAL_TO_STRING': False,
    # 'EXCEPTION_HANDLER': 'utils.custom_exception_handler.custom_exception_handler'
}

# 跨域增加忽略
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
    'VIEW',
)

CORS_ALLOW_HEADERS = (
    'XMLHttpRequest',
    'X_FILENAME',
    'accept-encoding',
    'authorization',
    'content-type',
    'accept',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'Pragma',
)

# 首页显示服务器、python、django、simpleui相关信息
SIMPLEUI_HOME_INFO = False
#
# AUTHENTICATION_BACKENDS = [
#     'user.utils.UsernameMobileAuthBackend',
# ]


STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, '../static'),
)
STATIC_ROOT = os.path.join(BASE_DIR, '../staticfiles')

FILE_UPLOAD_PERMISSIONS = 0o644
