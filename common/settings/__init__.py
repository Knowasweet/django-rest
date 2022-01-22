import os
from pathlib import Path

from .rest_framework import *

DEBUG = int(os.environ.get("DEBUG", default=True))

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get("SECRET_KEY", default='django-insecure-s6x2izcedrz&3ppz8a*+77vmarij(2jukfb5c^j7brtq_#t46d')

ROOT_URLCONF = 'common.urls'

if os.environ.get('DJANGO_ALLOWED_HOSTS') is not None:
    ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS').split(" ")
else:
    ALLOWED_HOSTS = ['*']

# Application definition
DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
    'drf_yasg',
    'djoser',
    'django_filters',
    'rest_framework',
    'rest_framework.authtoken',
)

LOCAL_APPS = (
    'users.apps.UsersConfig',
    'film_crews.apps.FilmCrewsConfig',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

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

WSGI_APPLICATION = 'common.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django-backend',
        'USER': 'postgres',
        'PASSWORD': '54321',
        'HOST': 'db',  # 'localhost'
        'PORT': '5432'
    }
}

# Password validation
AUTH_USER_MODEL = "users.User"

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR / 'static')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
