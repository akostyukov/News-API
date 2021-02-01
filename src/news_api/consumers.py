from celery import bootsteps
from kombu import Consumer

from news.tasks import fresh_news_save
from news_api.celery import app
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

    def save_news(self, body, message):
        news = body.get(list(body.keys())[0])
        fresh_news_save.delay(news)
        message.ack()


app.steps["consumer"].add(FreshNewsConsumerStep)
