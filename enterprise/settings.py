"""
Django settings for enterprise project.

Generated by 'django-admin startproject' using Django 4.0.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-h#+evkxj5clqu3+xtj4%ynj25m&h&)l035!evpc)z0=zs--vg8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application References
# https://docs.djangoproject.com/en/3.2/ref/settings/#std:setting-INSTALLED_APPS
DJANGO_APPS = [
    # Add your apps here to enable them
    'django.contrib.admin', # Chapter 6 - Exploring the Django Admin Site
    'django.contrib.auth', # Chapter 2 - Project Configuration
    'django.contrib.contenttypes', # Chapter 2 - Project Configuration
    'django.contrib.sessions', # Chapter 7 - Django Messages Framework
    'django.contrib.messages', # Chapter 7 - Django Messages Framework
    'django.contrib.staticfiles', # Chapter 2 - Project Configuration
]

THIRD_PARTY_APPS = [
    # Introduced in Chapter 9, can be turned on in all previous chapters without disrupting
    # those exercises. Turn Off/Comment Out For the First Half of Chapter 9
    #'debug_toolbar',

    'django_extensions', # Chapter 2 - Project Configuration
    #'address', # Chapter 3 - Django Models
    'djmoney', # Chapter 3 - Django Models
    #'phone_field', # Chapter 3 - Django Models
    #'rest_framework', # Chapter 8 - Django REST Framework
    #'rest_framework.authtoken', # Chapter 8 - Django REST Framework
]

#if DEBUG:
#    # Introduced in Chapter 9, can be turned on in all previous chapters without disrupting
#    # those exercises. Turn Off/Comment Out For the First Half of Chapter 9
#    THIRD_PARTY_APPS[0] = 'debug_toolbar'

'''
Only use chapter 1 to go back and practice generating diagrams in that chapter,
Chapter 3 - 10, will need to comment out chapter_1 in order to use those chapters without
errors. You can always practice generating diagrams on other apps/models as well. The reason
errors will result, is because in Chapter 3 we practiced changing the AUTH_USER_MODEL setting
to now point to the Seller model instead of the default User model. A model in Chapter 1's
example points to the original User model. Proceed with caution!
'''
LOCAL_APPS = [
    #'enterprise.chapter_1',

    'enterprise.chapter_2',
    'enterprise.chapter_3',
    #'enterprise.chapter_4',
    #'enterprise.chapter_5',
    #'enterprise.chapter_6',
    #'enterprise.chapter_7',
    #'enterprise.chapter_8',
    #'enterprise.chapter_9',
    #'enterprise.chapter_10',
]

# Chapter 2 - Project Configuration
#### MERGE ALL APPS ####
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'enterprise.urls'

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

WSGI_APPLICATION = 'enterprise.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
#    }
#}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db_packt-enterprise',
        'USER': 'adriano',
        'PASSWORD': '19550411*scF',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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

# Chapter 3 - Custom User Model - This Value is Needed for Chapter 4 - 10
#AUTH_USER_MODEL = 'chapter_3.Seller'


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Chapter 3 - Third Party Field Type
# Django-Money Field Package
CURRENCIES = ('USD', 'EUR')
CURRENCY_CHOICES = [
    ('USD', 'USD $'),
    ('EUR', 'EUR €'),
]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
