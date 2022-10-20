#!/bin/sh

python manage.py migrate
python manage.py collectstatic --no-input --clear

gunicorn edi_ems_api.wsgi:application --bind 0.0.0.0:8000

# exec "$@"