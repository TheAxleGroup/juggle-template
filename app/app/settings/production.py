# app/app/settings/production.py
from .base import *
import django_heroku

INSTALLED_APPS += [
    'wagtailcache',
]

DJANGO_ROOT = '/home/app/'

SECRET_KEY = os.environ.get("SECRET_KEY")

# Database PostgreSQL
# django_heroku.settings(locals())
DATABASES['default'] = os.environ.get('DATABASE_URL')

DEBUG = os.environ.get("DEBUG") == 'True'
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")
CSRF_TRUSTED_ORIGINS = ALLOWED_HOSTS

# AWS SETTINGS #
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_BUCKET_NAME')
AWS_S3_REGION_NAME = os.environ.get('AWS_REGION')
AWS_CLOUDFRONT_DISTROBUTION_ID = os.environ.get('AWS_CLOUDFRONT_DISTROBUTION_ID')
AWS_CLOUDFRONT_SUBDOMAIN = os.environ.get('AWS_CLOUDFRONT_SUBDOMAIN')
AWS_LOCATION = 'public'
AWS_QUERYSTRING_AUTH = False
AWS_S3_FILE_OVERWRITE = False

# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
COMPRESS_ROOT = STATIC_ROOT

STATICFILES_STORAGE = 'app.storage.CachedS3Boto3Storage'
COMPRESS_STORAGE = STATICFILES_STORAGE

# STATIC_URL = 'http://' + AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com/'
AWS_S3_CUSTOM_DOMAIN = '%s.cloudfront.net' % AWS_CLOUDFRONT_SUBDOMAIN
STATIC_URL = 'https://%s/' % AWS_S3_CUSTOM_DOMAIN
COMPRESS_URL = STATIC_URL
# ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

# AWS cache settings, don't change unless you know what you're doing:
AWS_EXPIRY = 60 * 60 * 24 * 7
AWS_IS_GZIPPED = True

control = 'max-age=%d, s-maxage=%d, must-revalidate' % (AWS_EXPIRY, AWS_EXPIRY)
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': control,
}

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True

EMAIL_HOST = os.environ.get('MAILGUN_SMTP_SERVER')
EMAIL_PORT = os.environ.get('MAILGUN_SMTP_PORT')
EMAIL_HOST_USER = os.environ.get('MAILGUN_SMTP_LOGIN')
EMAIL_HOST_PASSWORD = os.environ.get('MAILGUN_SMTP_PASSWORD')
EMAIL_USE_TLS = True
SITE_ID = 1


MIDDLEWARE = ('wagtailcache.cache.UpdateCacheMiddleware',) + MIDDLEWARE + ('wagtailcache.cache.FetchFromCacheMiddleware',)

REDIS_URL = os.environ.get("REDIS_URL")
CACHES = {
    'default': {
        'BACKEND': 'wagtailcache.compat_backends.django_redis.RedisCache',
        'LOCATION': '%s' % REDIS_URL,
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    },
}

CLOUDFLARE_API_TOKEN = os.environ.get('CLOUDFLARE_API_TOKEN')
CLOUDFLARE_ZONE_ID = os.environ.get('CLOUDFLARE_ZONE_ID')

WAGTAILFRONTENDCACHE = {
    'cloudflare': {
        'BACKEND': 'wagtail.contrib.frontend_cache.backends.CloudflareBackend',
        'BEARER_TOKEN': CLOUDFLARE_API_TOKEN,
        'ZONEID': CLOUDFLARE_ZONE_ID,
    },
    # 'cloudfront': {
    #     'BACKEND': 'wagtail.contrib.frontend_cache.backends.CloudfrontBackend',
    #     'DISTRIBUTION_ID': AWS_CLOUDFRONT_DISTROBUTION_ID,
    # },
}

WAGTAIL_ENABLE_UPDATE_CHECK = False

try:
    from .local import *
except ImportError:
    pass
