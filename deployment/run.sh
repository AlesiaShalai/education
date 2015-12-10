#!/bin/sh
. /home/{{ app_name }}/env.sh

cd /home/{{ app_name }}/{{ app_name }}
exec gunicorn -b :{{ proxy_port }} task3.wsgi:application
