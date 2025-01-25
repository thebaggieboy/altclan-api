import os
from datetime import timedelta
from pathlib import Path
from dotenv import load_dotenv
import dj_database_url
# Build paths inside the project like this: BASE_DIR / 'subdir'.
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['altclan-api-v1.onrender.com', 'localhost', '127.0.0.1', 'altclan-api.onrender.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'core.apps.CoreConfig',
    'brands.apps.BrandsConfig',
    'accounts.apps.AccountConfig',
    'transactions.apps.TransactionsConfig',
    'reviews',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'djoser',
    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',
    'dj_rest_auth.registration',
    'corsheaders',
    'crispy_forms',
    'rest_framework_simplejwt',
 
]


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    
    'corsheaders.middleware.CorsPostCsrfMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'altclan.urls'

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

WSGI_APPLICATION = 'altclan.wsgi.application'


# Database
# docs.djangoproject.com/en/4.1/ref/settings/#databases


DATABASES = {
       'default': dj_database_url.config(default='postgres://postgresql:/postgresql://altclan_v0om_user:hMnufxoMLehsmUQXHPUX36KIdZnlFK3X@dpg-cu9lpvtsvqrc73dh9lk0-a.oregon-postgres.render.com/altclan_v0om')
}



# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT =os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
CRISPY_TEMPLATE_PACK = 'bootstrap5'
SITE_ID = 1

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.

    'DEFAULT_AUTHENTICATION_CLASSES': [
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
     'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny'
    ],
   
}

SESSION_COOKIE_SAMESITE = 'None'
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SAMESITE = 'None'
CSRF_COOKIE_SECURE = True

CSRF_TRUSTED_ORIGINS = ['https://*.altclan.store', 'https://*.altclan.com', 'https://altclan.com',  'https://altclanstore.vercel.app', 'https://altclan.store',  'https://*.altclan.store',  'http://altclan-api.onrender.com',  'http://localhost:8000','http://127.0.0.1:8000', 'http://localhost:3000','http://127.0.0.1:3000',]

REST_AUTH = {
    
    'USE_JWT': True,
    'JWT_AUTH_COOKIE': 'token',
    'JWT_AUTH_REFRESH_COOKIE': 'refresh-token',
    'JWT_AUTH_COOKIE_USE_CSRF':False,
    'JWT_AUTH_SAMESITE': 'Lax',
    'JWT_AUTH_SECURE': False,
    'JWT_AUTH_HTTPONLY': True,
}
AUTHENTICATION_BACKENDS = ( 
	'django.contrib.auth.backends.ModelBackend', 
	'allauth.account.auth_backends.AuthenticationBackend', 
)

SIMPLE_JWT = {
    'AUTH_HEADER_TYPES':('JWT', 'Bearer'),
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
}

CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_METHODS = [
'DELETE',
'GET',
'OPTIONS',
'PATCH',
'POST',
'PUT',
]

CORS_ALLOW_HEADERS = [
'accept',
'accept-encoding',
'authorization',
'content-type',
'dnt',
'origin',
'user-agent',
'x-csrftoken',
'x-requested-with',
]



CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    'http://127.0.0.1:3000',
    'http://localhost:8000',
    'http://127.0.0.1:8000',
    'http://altclan.com',
    'https://altclan.com',
    'https://altclan-api.onrender.com',
    'https://api.cloudinary.com'
    
]

CORS_ORIGIN_WHITELIST = [
    
    'http://localhost:3000',
    'http://127.0.0.1:3000',
    'http://localhost:8000',
    'http://127.0.0.1:8000',
    'http://altclan.com',
    'https://altclan.com',
    'https://altclan-api.onrender.com',
    'https://api.cloudinary.com'
    
    
    
]

CORS_ALLOW_CREDENTIALS = True
CORS_REPLACE_HTTPS_REFERER = True
ACCOUNT_USER_MODEL_USERNAME_FIELD = 'email'
AUTH_USER_MODEL = 'accounts.AccountUser'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION ='optional'
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True


# DJOSER SETTINGS
DJOSER = {
    'PASSWORD_RESET_CONFIRM_URL': '#/password/reset/confirm/{uid}/{token}/',
    'USERNAME_RESET_CONFIRM_URL': '#/username/reset/confirm/{uid}/{token}/',
    'ACTIVATION_URL': '#/activate/{uid}/{token}/',
    'SEND_ACTIVATION_EMAIL': True,
    'SERIALIZERS': {
       'user_create':'accounts.serializers.UserCreateSerializer' 
    },
}
# Email SMTP Settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST=os.getenv("EMAIL_HOST")
EMAIL_PORT = 587
EMAIL_HOST_USER=os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD=os.getenv("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = True
#EMAIL_USE_SSL = False