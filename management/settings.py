from pathlib import Path

import environ
import os

env=environ.Env()
env.read_env()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = env('SECRET_KEY')
DEBUG = True
ALLOWED_HOSTS = ['*', '127.0.0.1:8000']

INSTALLED_APPS = [
    'jazzmin',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'macros',
    'crispy_forms',
    'crispy_bootstrap4',
    'django_sass',
    'django_bootstrap_icons',   
    
    'psycopg2',

    'channels',
    'rest_framework',

    "students",
    'Users',
    'utils',
]



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'management.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / "templates",
        ],
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

WSGI_APPLICATION = 'management.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env("DB_NAME"), 
        'USER': env("DB_USER"),
        'PASSWORD': env("DB_PASSWORD"),
        'HOST': env("DB_HOST"), 
        'PORT': env("DB_PORT"),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True
USE_TZ = True

#Crispy-forms-stylesheets

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"
CRISPY_TEMPLATE_PACK = "bootstrap4"

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_ROOT = [BASE_DIR, 'media']
MEDIA_URL = '/media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL='Users.user'

LOGIN_URL = "user/login/"
LOGIN_REDIRECT_URL = "/"

# APPEND_SLASH= True 

#E-mail config
# EMAIL_BACKEND='django.core.mail.backend.smtp.EmailBackend'


#Caches

CACHES ={
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}


REST_FRAMEWORK = { 
  
    'DEFAULT_CACHE_BACKEND': 'default',
    # 'DEFAULT_AUTHENTICATION_CLASSES': { 
    #     'rest_framework.authentication.BasicAuthentication', 
    # },
    # 'DEFAULT_THROTTLE_CLASSES': { 
    #     'rest_framework.throttling.AnonRateThrottle', 
    #     'rest_framework.throttling.UserRateThrottle'
    # }, 
    # 'DEFAULT_THROTTLE_RATES': { 
    #     'anon': '2/day', 
    #     'user': '5/day'
    # }, 
}

from .custom_ad import JAZZMIN_SETTINGS, JAZZMIN_UI_TWEAKS

CRISPY_CLASS_CONVERTERS = {
    # 'textinput': "form-control google-input",
    # 'emailinput': "form-control google-input",
}