from conf.settings.base_setting import *

with open("secret.json", "r", encoding="UTF-8") as file:
    secret_key_list = json.loads(file.read())

def get_secret(key, secret_key_list=secret_key_list):
    try:
        return secret_key_list[key]
    except KeyError:
        raise ImproperlyConfigured("{}오류".format(key))


SECRET_KEY = get_secret("secret_DJANGO")

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}