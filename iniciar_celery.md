PATH=$PATH:/usr/local/sbin
sudo rabbitmq-server -detached
sudo rabbitmqctl status
sudo rabbitmqctl stop

GMAIL_HOST_USER=ricardo0100@gmail.com GMAIL_HOST_PASSWORD=macacavesga.13 DJANGO_SETTINGS_MODULE=main.settings celery -A tasks worker --loglevel=info
