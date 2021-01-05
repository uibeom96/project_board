from conf.settings.base_setting import *

with open("secret.json", "r", encoding="UTF-8") as file:
    secret_key_list = json.loads(file.read())

def get_secret(key, secret_key_list=secret_key_list):
    try:
        return secret_key_list[key]
    except KeyError:
        raise ImproperlyConfigured("{}오류".format(key))


SECRET_KEY = get_secret("secret_DJANGO")

DEBUG = False

ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': get_secret("secret_Deploy_ENGINE"),
        'NAME': get_secret("secret_Deploy_NAME"),
        "USER": get_secret("secret_Deploy_USER"),
        "PASSWORD": get_secret("secret_Deploy_PASSWORD"),
        "HOST":  get_secret("secret_Deploy_HOST"),
        "PORT": get_secret("secret_Deploy_PORT"),
    }
}