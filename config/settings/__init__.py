import os


if 'local' in os.environ.get('DJANGO_SETTINGS_MODULE'):
    from config.settings.local import *  # noqa
else:
    from config.settings.prod import *  # noqa
