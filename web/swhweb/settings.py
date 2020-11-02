"""
Django settings for swhweb project.

Generated by 'django-admin startproject' using Django 2.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""
# For configuring logging
import logging

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# This value should be overwritten in local_settings.py
SECRET_KEY = "zd6^l28fyl08rd!$f9g1g!r!8opk+a6n9irke3+(@ht*sgp(gt"

# SECURITY WARNING: don't run with debug turned on in production!
# This value should be overwritten in local_settings.py
DEBUG = True

# This value should be overwritten in local_settings.py
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "system.apps.SystemConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "swhweb.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "swhweb.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "America/Los_Angeles"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# If this is set to true, then globally all numbers are displayed with
# a thousand separator (the character used for that depends on the locale)
USE_THOUSAND_SEPARATOR = False

# Alternatively you can add 'django.contrib.humanize' to INSTALLED_APPS
# and use this in your template only where you want it:
# {% load humanize %}
# {{ my_number|intcomma }}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

# Look at these places for static files, to be copied to top level static
# folder (which is not included in version control) with command
#  $ python manage.py collectstatic
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "./system/static/"),  # app specific statics
    os.path.join(
        BASE_DIR, "./swhweb/static/"
    ),  # statics not tied to any specific app
]

# Read information from local_settings.py and overwrite values specified in this file
# Keep these lines at the end of the file
try:
    from .local_settings import *

    # print("SUCCESSFULLY IMPORTED LOCAL SETTINGS")
except ImportError:
    print("NOT ABLE TO IMPORT LOCAL SETTINGS")

# Configure logging (choose one of the two)
# LOG_LEVEL = logging.DEBUG if DEBUG else logging.INFO
LOG_LEVEL = logging.INFO if DEBUG else logging.WARNING
logging.basicConfig(
    level=LOG_LEVEL,
    format="%(asctime)s %(name)s - %(levelname)s: %(message)s",
    datefmt="[%d/%b/%Y %H:%M:%S]",
)

# Define path to SWH database
SWH_DATABASE = os.path.join(
    BASE_DIR, "..", "mswh", "comm", "swh_system_input.db"
)

# Define data source to use for climate objects, valid values are 'cec' and 'tmy3'
CLIMATE_DATA_SOURCE = "cec"