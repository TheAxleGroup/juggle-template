from .base import *

SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = os.environ.get("DEBUG") == 'True' or True
ALLOWED_HOSTS = ["*"]

# Database PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': os.environ.get("SQL_ENGINE"),
        'NAME': os.environ.get("SQL_DATABASE"),
        'USER': os.environ.get("SQL_USER"),
        'PASSWORD': os.environ.get("SQL_PASSWORD"),
        'HOST': os.environ.get("SQL_HOST"),
        'PORT': os.environ.get("SQL_PORT"),
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
AWS_BUCKET_ROOT = ''

try:
    from .local import *
except ImportError:
    pass