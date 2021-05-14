#!/usr/bin/env sh

python ./manage.py migrate
python ./manage.py collectstatic --noinput
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@myproject.com', 'password')" | python manage.py shell
gunicorn --forwarded-allow-ips=* --bind 0.0.0.0:8000 -w 2 InvBase.wsgi:application