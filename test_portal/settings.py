"""
Django settings for test_portal project.

Generated by 'django-admin startproject' using Django 5.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os
from datetime import timedelta  # Added for token lifetime configuration

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-i9d_-+e(bfi4x*lzbc2o@7j)&$kk#2!qo9h87ai8ke+44u=10_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = []
# ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")
# ALLOWED_HOSTS = ["127.0.0.1", "localhost", "https://petroxtestbackend.onrender.com"]
ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    "petroxtestbackend.onrender.com",  # Add the Render hostname without protocol
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'exams',
    'corsheaders',
    'channels',
]

ASGI_APPLICATION = 'test_portal.asgi.application'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

# SIMPLE_JWT configuration for token lifetimes
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=1),   # Access token expires after 1 hour
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),     # Refresh token expires after 7 days
}

# ---------------------------
# Email Settings
# ---------------------------
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 465
EMAIL_USE_TLS = False       # Using SSL, so disable TLS
EMAIL_USE_SSL = True
EMAIL_HOST_USER = 'thecbsteam8@gmail.com'
EMAIL_HOST_PASSWORD = 'rvis xrgl qztb ednr'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
# ---------------------------

CORS_ALLOW_ALL_ORIGINS = True

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # <-- this belongs here
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'test_portal.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI_APPLICATION = 'test_portal.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# Example using PostgreSQL on Render with internal connection string:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'petroxdatebase2',  # your database name
        'USER': 'petroxdatebase2_user',  # your database user
        'PASSWORD': 'zLyo6YIHVF93l8pWq3129Vz7Lraozivk',  # your database password
        'HOST': 'dpg-cusacpqj1k6c73f2u830-a',  # internal hostname
        'PORT': '5432',  # default PostgreSQL port
    }
}

CSRF_TRUSTED_ORIGINS = [
    "https://petroxtestbackend.onrender.com",
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
USE_TZ = True
TIME_ZONE = 'UTC'  # Or your preferred timezone

# CHANNEL_LAYERS configuration for Channels using Redis
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": ["redis://red-cukj92tumphs73belin0:6379"],
        },
    },
}

