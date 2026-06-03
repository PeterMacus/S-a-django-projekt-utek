#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate


if [ -n "$admin" ] && [ -n "$admin" ]; then
    python manage.py createsuperuser --no-input || true
fi