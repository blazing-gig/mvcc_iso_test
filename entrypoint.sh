#!/bin/sh

# shellcheck disable=SC2046
echo $(pwd)

ls -al

. /opt/venv/bin/activate

echo $PATH

echo $(python --version)

echo $DATABASE_URL

cd /code

python manage.py migrate

python manage.py runserver 8000