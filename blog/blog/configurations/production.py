from .base import *

# TODO: Dejar solo el dominio de prod
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'mi-dominio-prod-ejemplo.com']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# TODO: Cambiar la config de la base de datos para prod
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',

        # 'ENGINE': 'django.db.backends.postgresql',
        # 'ENGINE': 'django.db.backends.mysql',

        # 'NAME': os.getenv('DB_NAME'),
        # 'USER': os.getenv('DB_USER'),
        # 'PASSWORD': os.getenv('DB_PASSWORD'),
        # 'HOST': os.getenv('DB_HOST'),
        # 'PORT': os.getenv('DB_PORT'),
    }
}

os.environ['DJANGO_PORT'] = '8080'