#!/usr/bin/env python
import os
import subprocess
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sayhello.settings")
    if sys.argv[1] == 'runserver':
        wsgi = __import__('sayhello.settings').settings.WSGI_APPLICATION
        env = os.environ.copy()
        env['PYTHONPATH'] = os.getcwd()
        subprocess.check_call(["twist", "web", "--wsgi", wsgi] + sys.argv[2:],
                              env=env)
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
