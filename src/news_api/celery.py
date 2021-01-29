import os

from celery import Celery

from news_api.consumers import FreshNewsConsumerStep

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "news_api.settings")

app = Celery("news_api", broker="amqp://rabbitmq:rabbitmq@rabbitmq:5672")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()

app.steps["consumer"].add(FreshNewsConsumerStep)
