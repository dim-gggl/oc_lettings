#!/bin/sh
python manage.py migrate --no-input
exec gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:8000
