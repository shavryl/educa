from .base import *

DEBUG = False

ADMINS = (
    ('Stanislav G', 'gavrilchenko.stanislav@gmail.com'),
)

ALLOWED_HOSTS = ['*']

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': 'educa',
       'USER': 'root',
       'PASSWORD': 'root',
       'HOST': 'localhost',
   }
}
