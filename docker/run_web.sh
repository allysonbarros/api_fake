#!/bin/sh

cd /app
su -m app -c "python manage.py migrate"
su -m app -c "python manage.py collectstatic --noinput"
su -m app -c "gunicorn api_faker.wsgi -w 2 -b 0.0.0.0:8000"
