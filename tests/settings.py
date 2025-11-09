import os

from wagtail.test.settings import *  # noqa: F403

INSTALLED_APPS = INSTALLED_APPS + [  # noqa: F405
    "wagtail_block_components",
    "tests",  # Add tests app so wagtail_hooks.py is discovered
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

# Add test templates directory
TEMPLATES[0]["DIRS"].insert(0, os.path.join(os.path.dirname(__file__), "templates"))  # noqa: F405
