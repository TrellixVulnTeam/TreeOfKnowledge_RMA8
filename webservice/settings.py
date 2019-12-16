"""
Django settings for webservice project.

Generated by 'django-admin startproject' using Django 2.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
from decouple import config

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4#trl*=#otl7kt&sz7$lf%v0l&a0-)@oawykk4%lgv2t$ou7^x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS  = ['*', 'datascienceforgood-aalen.herokuapp.com','Treeofknowledge.eu-central-1.elasticbeanstalk.com']


# Application definition

INSTALLED_APPS = [
	'collection', 
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'registration',
    'bootstrap3',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'webservice.urls'

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

WSGI_APPLICATION = 'webservice.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
if 'RDS_HOSTNAME' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }



# EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend'
# MAILER_EMAIL_BACKEND = EMAIL_BACKEND
# EMAIL_HOST = 'mail.gmx.net'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'bene3@gmx.net'
# EMAIL_HOST_PASSWORD = '1q2W3e4R5t6Z'
# DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
# DEFAULT_TO_EMAIL = EMAIL_HOST_USER
# EMAIL_USE_TLS = True
# EMAIL_USE_SSL = False


# EMAIL_HOST = 'mail.gmx.net'
# EMAIL_PORT = 465
# EMAIL_HOST_USER = 'bene3@gmx.net'
# DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
# SERVER_MAIL = EMAIL_HOST_USER
# EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
# EMAIL_USE_TLS = False
# EMAIL_USE_SSL = True
# EMAIL_TIMEOUT = 3600
# DEFAULT_CHARSET = 'utf-8'
# EMAIL_USE_LOCALTIME = True

EMAIL_HOST = 'smtp.fastmail.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'benedikt@kleppmann.de'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_MAIL = EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
EMAIL_TIMEOUT = 3600
DEFAULT_CHARSET = 'utf-8'
EMAIL_USE_LOCALTIME = True


# EMAIL_HOST = 'smtp.sendgrid.net'
# EMAIL_PORT = 465
# EMAIL_HOST_USER = 'apikey'
# DEFAULT_FROM_EMAIL = 'noreply@treeofknowledge.ai'
# SERVER_MAIL = 'noreply@treeofknowledge.ai'
# EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
# EMAIL_USE_TLS = False
# EMAIL_USE_SSL = True
# EMAIL_TIMEOUT = 3600
# DEFAULT_CHARSET = 'utf-8'
# EMAIL_USE_LOCALTIME = True






# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# STATIC_ROOT = 'staticfiles'
STATICFILES_DIRS = (
	os.path.join(BASE_DIR, 'static'),
)

REGISTRATION_OPEN = True
ACCOUNT_ACTIVATION_DAYS = 7
# REGISTRATION_AUTO_LOGIN = True


# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'Tree of Knowledge Team <noreply@treeofknowledge.ai>'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'BenediktKleppmann'
# EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_HOST_PASSWORD = 'ACUp77vppoh4wHhUICeT'
EMAIL_USE_TLS = False
# EMAIL_USE_SSL = True


LOGIN_REDIRECT_URL = "main_menu"
# LOGIN_URL = "accounts/login/"


DATA_UPLOAD_MAX_MEMORY_SIZE = 524288000