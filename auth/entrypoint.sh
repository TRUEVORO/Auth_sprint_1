#!/bin/sh

echo "Waiting for postgres..."
while ! nc -z "$POSTGRES_HOST" "$POSTGRES_PORT"; do
  sleep 0.1
done
echo "PostgreSQL started"

cd src || exit

gunicorn -c gunicorn/gunicorn.py -k gevent app:app
