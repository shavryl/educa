from .base import *

DEBUG = False

ADMINS = (
    ('Stanislav G', 'gavrilchenko.stanislav@gmail.com'),
)

ALLOWED_HOSTS = ['educaproject.com', 'www.educaproject.com']

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': 'educa',
       'USER': 'root',
       'PASSWORD': 'root',
       'HOST': 'localhost',
   }
}
