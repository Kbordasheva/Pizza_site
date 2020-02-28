# Pizza_site
simple Django pizza site

Usage:

1. Create in a root directory file myEnvVal.py:

import os


def setVar():
    os.environ['EMAIL_HOST_USER'] = 'Your_email@gmail.com'
    os.environ['EMAIL_HOST_PASSWORD'] = 'your_password'

2. ./manage.py runserver
