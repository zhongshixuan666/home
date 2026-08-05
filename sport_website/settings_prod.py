"""生产环境配置：通过环境变量覆盖关键项，基于 settings.py。"""

import os

from .settings import *  # noqa: F401,F403

DEBUG = False

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', SECRET_KEY)

ALLOWED_HOSTS = [
    h.strip()
    for h in os.environ.get('DJANGO_ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')
    if h.strip()
]

CSRF_TRUSTED_ORIGINS = [
    o.strip()
    for o in os.environ.get('DJANGO_CSRF_TRUSTED_ORIGINS', '').split(',')
    if o.strip()
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

STORAGES = {
    'default': {
        'BACKEND': 'django.core.files.storage.FileSystemStorage',
    },
    'staticfiles': {
        'BACKEND': 'whitenoise.storage.CompressedManifestStaticFilesStorage',
    },
}

_middleware = list(MIDDLEWARE)
if 'django.middleware.security.SecurityMiddleware' in _middleware:
    _middleware.insert(
        _middleware.index('django.middleware.security.SecurityMiddleware') + 1,
        'whitenoise.middleware.WhiteNoiseMiddleware',
    )
else:
    _middleware.insert(0, 'whitenoise.middleware.WhiteNoiseMiddleware')
MIDDLEWARE = _middleware

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
_https = os.environ.get('DJANGO_HTTPS', '0') == '1'
SESSION_COOKIE_SECURE = _https
CSRF_COOKIE_SECURE = _https
