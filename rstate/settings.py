import os
from pathlib import Path
from decouple import  config
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR   = Path(__file__).resolve().parent.parent
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG         = True
ALLOWED_HOSTS = ['65.1.151.181','*']


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rportal',
    'rblog',
    'ckeditor',
    'ckeditor_uploader'
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

ROOT_URLCONF    = 'rstate.urls'
AUTH_USER_MODEL = 'rportal.User'

TEMPLATES = [
    {
        'BACKEND'  : 'django.template.backends.django.DjangoTemplates',
        'DIRS'     : ['templates'],
        'APP_DIRS' : True,
        'OPTIONS'  : {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'rstate.wsgi.application'


CKEDITOR_JQUERY_URL  = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': None,
    },
}


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
   'default':{
      'ENGINE':'django.db.backends.sqlite3',
      'NAME'  : BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE     = 'UTC'
USE_I18N      = True
USE_L10N      = True
USE_TZ        = True



# Email Configurations
EMAIL_BACKEND           = config('EMAIL_BACKEND')
EMAIL_HOST              = config('EMAIL_HOST')
EMAIL_USE_TLS           = config('EMAIL_USE_TLS')
EMAIL_PORT              = config('EMAIL_PORT')
EMAIL_HOST_USER         = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD     = config('EMAIL_HOST_PASSWORD')



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
STATIC_URL        = '/static/'
STATICFILES_DIRS  = [os.path.join(BASE_DIR, 'static')]
MEDIA_URL         = '/media/'
MEDIA_ROOT        = os.path.join(BASE_DIR,'media')
STATIC_ROOT       = os.path.join(BASE_DIR,'files')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
