"""
Django settings for AI project.

Generated by 'django-admin startproject' using Django 2.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'j4l6xaj^1n)k2!a$=shn$zp1i0ga%pen+$5oqy%s=zqmag-g2_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'AI_qast.apps.AiQastConfig',
    # 'AI_check',

    'rest_framework',
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

ROOT_URLCONF = 'AI.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'AI.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',
        'NAME': 'qc',
        'USER': 'root',
        'PASSWORD': '123456',
        'PORT': 3306
    }
}


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

LANGUAGE_CODE = 'zh-hans'
# LANGUAGE_CODE = 'zh-cn'
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]


REST_FRAMEWORK = {
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.NamespaceVersioning',
}

LOG_DIR = os.path.join(BASE_DIR, 'log')

LOGGING = {
    'version': 1,
    'disable_existing_loggers':True,
    'formatters': {
        'standard_1': {
            'format': '-------[Pid:%(process)d] [Thid:%(thread)d] [%(name)s:%(lineno)d]  '
                      '[%(module)s:%(funcName)s] [%(levelname)s] [%(asctime)s]- %(message)s'},
        'standard': {
            'format': '------[%(levelname)s][%(name)s:%(lineno)d] [%(module)s:%(funcName)s][%(asctime)s]- %(message)s'}
        # 日志格式
    },
    'filters': {
    },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'default.log'),  # 日志输出文件
            'maxBytes': 1024 * 1024 * 5,  # 文件大小
            'backupCount': 5,  # 备份份数
            'encoding': 'utf8',
            'formatter': 'standard',  # 使用哪种formatters日志格式
        },
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'error.log'),
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'encoding': 'utf8',
            'formatter': 'standard',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        'request_handler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'request.log'),
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'encoding': 'utf8',
            'formatter': 'standard',
        }
    },
    'loggers': {
        'all': {
            'handlers': ['default','console'],
            'level': 'DEBUG',
            'propagate': False
        },
        'error': {
            'handlers': ['console', 'error'],
            'level': 'ERROR',
            'propagate': False
        },
        'django.request': {
            'handlers': ['request_handler'],
            'level': 'DEBUG',
            'propagate': False,
        }
    }
}




CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/9",
        # 'TIMEOUT': 60 * 30,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "SOCKET_CONNECT_TIMEOUT": 5,  # in seconds
            "SOCKET_TIMEOUT": 5,  # in seconds
            "CONNECTION_POOL_KWARGS": {"max_connections": 100}
        }
    }
}

#百度接口认证
APP_ID = ''
API_KEY = ''
SECRET_KEY = ''



#疑问句词库
Interrogative_library = [
    '吗','呢','？','为什么',
    '是不是','有没有','是不是这样','怎么样?','需要多久','多少',
    # '谁','何','哪儿','哪里','几时','几',
    # '怎么','怎','怎的','怎样','怎么样?','如何',
    #'难道','岂','居然','竟然','究竟','简直','难怪','反倒','何尝','何必'

]

cassandre_data = {
    'username': 'ntalker',
    'password': 'xiaoneng2015',
    'ip': ['192.168.30.211 '],
    'port': 9042,
    'new_create_keyspace':'quality',
    'query_keyspace':'xn_dolphin_1',

}

#分析模块的url
URL= "http://127.0.0.1:8000/api/v1/analysis/"
