# flake8: noqa
# pylint: skip-file
# type: ignore


from .staging_settings_modifications import *

DEBUG = os.getenv("DJANGO_DEBUG", "False") == "True"
ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "").split(",")

SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]
# generate your own secret key using
# import random, string
# print("".join(random.choice(string.printable) for _ in range(50)))
