from .base import *
import datetime

DEBUG = True

ALLOWED_HOSTS = []

# AUTHORIZATION_CODE_EXPIRE_SECONDS = 40

# SESSION_EXPIRE_AT_BROWSER_CLOSE = True
# SESSION_COOKIE_AGE = 40
# SESSION_SAVE_EVERY_REQUEST = True
# Application definition

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose0': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'verbose': {
            'format': "[%(asctime)s] [%(levelname)s] [%(name)s:%(lineno)s] [%(path)s] [%(ip)s] [%(user)s] [%(method)s] %(message)s",
            'datefmt': "%Y-%m-%d %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
        'verbose_dj': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%Y-%m-%d %H:%M:%S"
        },
    },
    'handlers': {

        'file_django': {
            'level': 'DEBUG',
            # 'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
            'class': 'logging.FileHandler',
            'filename': os.path.join(
                BASE_DIR, 'temp/logs',
                'dj%s.txt' % (datetime.datetime.now().strftime("%Y-%m-%d"))
            ),
            'formatter': 'verbose_dj'
        },
        'file_log': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(
                BASE_DIR, 'temp/logs',
                'log%s.txt' % (datetime.datetime.now().strftime("%Y-%m-%d"))
            ),
            'formatter': 'verbose'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose0'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file_django'],
            'propagate': False,
            'level': 'DEBUG',
        },
        'apps': {
            'handlers': ['file_log'],
            'level': 'DEBUG',
        },
    },
    'root': {
        'handlers': ['console', 'file_log', ],
        'level': 'INFO'
    },
}
