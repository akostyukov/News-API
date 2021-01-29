from celery import bootsteps
from kombu import Consumer

from news.tasks import fresh_news_save
from news_api.queues import fresh_news_queue


class FreshNewsConsumerStep(bootsteps.ConsumerStep):
    def get_consumers(self, channel):
        return [
            Consumer(
                channel,
                queues=[fresh_news_queue],
                callbacks=[self.save_news],
                accept=["json"],
            )
        ]

    def save_news(self, body: dict, message):
        fresh_news_save.delay(body.get(list(body.keys())[0]))
        message.ack()
