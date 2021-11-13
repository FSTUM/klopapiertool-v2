# flake8: noqa
# pylint: skip-file
# type: ignore

import logging.config

from template_project.settings import *

# staticfiles
MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# logging
LOGGING_CONFIG = None
LOGLEVEL = os.getenv("DJANGO_LOGLEVEL", "info").upper()
logging.config.dictConfig(
    {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "console": {
                "format": "%(asctime)s %(levelname)s "
                "[%(name)s:%(lineno)s] "
                "%(module)s %(process)d %(thread)d %(message)s",
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "console",
            },
        },
        "loggers": {
            "": {
                "level": LOGLEVEL,
                "handlers": ["console"],
            },
        },
    },
)
