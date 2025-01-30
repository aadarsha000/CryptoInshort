#!/bin/sh

# Apply database migrations
python manage.py migrate

# Add crontab tasks
python manage.py crontab add

daphne -b 0.0.0.0 -p 80 config.asgi:application