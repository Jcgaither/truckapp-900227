import os
from django.conf import settings

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!

EMAIL_HOST = os.environ['EMAIL_HOST']
EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
EMAIL_PORT = os.environ['EMAIL_PORT']
EMAIL_USE_TLS = 'True'

DEBUG = False

ALLOWED_HOSTS = ['.wheeldine.com']


LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'

SERIALIZATION_MODULES = {
    'geojson': 'djgeojson.serializers'
}

TIME_INPUT_FORMATS = ['%I:%M', '%I:%M%p', '%I:%M %p', '%I', '%p',]

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.gis',
    'envelope',
    'djstripe',
    'haystack',
    'whoosh',
    'trucks',
    'profiles',
    'rest_framework',
    'rest_framework_gis',
    'allauth',
    'allauth.account',
    'djgeojson',
    'localflavor',
    'permission',
    'sorl.thumbnail',
    'actstream',


)


ACTSTREAM_SETTINGS = {
    'FETCH_RELATIONS': True,
    'USE_PREFETCH': True,
    'USE_JSONFIELD': False,
    'GFK_FETCH_DEPTH': 1,
}

HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
    },
}

STRIPE_PUBLIC_KEY = os.environ["STRIPE_PUBLIC_KEY"]
STRIPE_SECRET_KEY = os.environ["STRIPE_SECRET_KEY"]
DJSTRIPE_SEND_INVOICE_RECEIPT_EMAILS = False
DJSTRIPE_PLANS = {
    "monthly": {
        "stripe_plan_id": "pro-monthly",
        "name": "WheelDine Premium",
        "description": "Monthly Subscription",
        "price": 1499,  # $14.99
        "currency": "usd",
        "interval": "month"
    },
    "yearly": {
        "stripe_plan_id": "pro-yearly",
        "name": "WheelDine Premium",
        "description": "Annual Subscription",
        "price": 15999,  # $159.00
        "currency": "usd",
        "interval": "year"
    }

}



ENVELOPE_EMAIL_RECIPIENTS = (
    'contact@wheeldine.com',
    )

SITE_ID = 3
SOCIALACCOUNT_PROVIDERS = \
    {'facebook':
       {'METHOD': 'oauth2',
        'SCOPE': ['email'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'FIELDS': [
            'id',
            'email',
            'name',
            'first_name',
            'last_name',
            'verified',
            'locale',
            'timezone',
            'link',
            'gender',
            'updated_time'],
        'EXCHANGE_TOKEN': True,
        'VERIFIED_EMAIL': False,
        'VERSION': 'v2.4'}}

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    # 'djstripe.middleware.SubscriptionPaymentMiddleware',

)

# DJSTRIPE_SUBSCRIPTION_REQUIRED_EXCEPTION_URLS = (
#     'account_signup',
#     'home',
#     'base_truck_create',
#     'plus_truck_delete',
#     'map',
#     'select_form',
#     'profile',
#     'delete_trucks',
#     'truck_ranking',
#     'plus_truck_detail',
#     'accounts',
#     'admin',
#     'account_signup',
#     'account_login',
#     'account_logout',
#     'account_change_password',
#     'account_set_password',
#     'account_inactive',
#     'actstream_follow',
#     'actstream_unfollow',
#     'ptl',
#     'ptd',
#     'premium_data',
#     'base_data',
#     "account_signup",
#     "account_login",
#     "account_logout",
#     "account_change_password",
#     "account_set_password",
#     "account_inactive",
#     "account_email",
#     "account_email_verification_sent",
#     "account_confirm_email",
#     "account_reset_password",
#     "account_reset_password_done",
#     "account_reset_password_from_key",
#     "account_reset_password_from_key_done",
#     "admin",
#     "envelope-contact",
#     "pricing,"
#     "add_feedback"
#     "feedback"
#     "event_detail"
#     "event_create"
#
#     )




ROOT_URLCONF = 'truckapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
                'django.core.context_processors.request',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = (

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    'permission.backends.PermissionBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',

)

WSGI_APPLICATION = 'truckapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
#



DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': os.environ['DATABASE_NAME'],
        'USER': os.environ['DATABASE_USER'],
        'PASSWORD': os.environ['DATABASE_PASSWORD'],
        'HOST':os.environ['DATABASE_HOST'],
        'PORT':os.environ['DATABASE_PORT']
    }
}





# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'EST'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'


STATICFILES_DIRS = (

    os.path.join(BASE_DIR, 'static'),

)


STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static_in_env', 'staticfiles' )


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'media_cdn')
