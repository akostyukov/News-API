import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "news_api.settings")

app = Celery("app", broker="amqp://rabbitmq:rabbitmq@rabbitmq:5672", include=['news_api.consumers'])

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()
