import os, django


def setup_django_env():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings")
    django.setup()


def check_db_connection():
    from django.db import connection

    if connection.connection:
        #NOTE: (zacky, 2016.MAR.21st) IF CONNECTION IS CLOSED BY BACKEND, CLOSE IT AT DJANGO, WHICH WILL BE SETUP AFTERWARDS.
        if not connection.is_usable():
            connection.close()
