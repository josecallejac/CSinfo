from pathlib import Path
import os


BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/


SECRET_KEY= 'django-insecure-1+wx&mi-n^o2ao#j$5c)67qo%c^%4#@66v+0eo(d+u6y-093*)'
DEBUG = True

#TAILWIND_DEV_MODE=True

ALLOWED_HOSTS = []





# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'compressor',
    'ckeditor',
   

    'widget_tweaks',

    'crispy_forms',
    'crispy_bootstrap5',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'core',
    'csinfo',

    'tailwind',
    'theme',

    'django_browser_reload',
    'accounts.apps.AccountsConfig',
    'hltv',

    'rest_framework',
    'coreapi',
    'blog',

]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

TAILWIND_APP_NAME = 'theme'
INTERNAL_IPS = [
    "127.0.0.1",
]

EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend'


NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"

AUTHENTICATION_BACKENDS = [

    'django.contrib.auth.backends.ModelBackend',

    'allauth.account.auth_backends.AuthenticationBackend',
]



ACCOUNT_FORMS = {
    'signup': 'core.forms.CustomSignupForm',
    
    

}

SITE_ID = 1

ACCOUNT_AUTHENTICATION_METHOD = "username_email"
#ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_UNIQUE = True
#Siosi debe verificar para poder entrar a la pagina
#ACCOUNT_EMAIL_VERIFICATION = "mandatory"
AUTH_USER_MODEL = "accounts.User"
#ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 3
#ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 300
#LOGIN_URL = "account_login"

LOGIN_REDIRECT_URL = "/"
ACCOUNT_LOGOUT_ON_GET = True






MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django_browser_reload.middleware.BrowserReloadMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',    
                
                'blog.processors.ctx_dic_about',
                'blog.processors.ctx_dic_category',    
                
                
            ],
        },
    },
]



WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'csinfo',
        'USER': 'postgres',
        'PASSWORD': '123',
        'HOST': 'localhost',
        'PORT':'5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'es-cl'

TIME_ZONE = 'America/Santiago'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema'
}
