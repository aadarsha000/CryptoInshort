#!/bin/sh

# Apply database migrations
python manage.py migrate

# Add crontab tasks
python manage.py crontab add

gunicorn config.wsgi:application -b 0.0.0.0:80 --workers 3