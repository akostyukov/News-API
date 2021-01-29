from hashlib import md5

from celery import shared_task

from news_api.queues import news_hash_queue


@shared_task
def send_hash(producer=None):
    from news.models import News
    from news_api.celery import app

    try:
        last_news = md5(News.objects.latest("date_time").header.encode()).hexdigest()
        print(
            f"@@@@@@@@@@@@@@@@@@@@@@@@ - {News.objects.latest('date_time').header} - @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
        )
    except:
        print(
            f"@@@@@@@@@@@@@@@@@@@@@@@@@@@@ - last_news is NONE - @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
        )
        last_news = None

    with app.producer_or_acquire(producer) as producer:
        producer.publish(
            {"hash": last_news},
            serializer="json",
            exchange=news_hash_queue.exchange,
            routing_key="news_hash",
            declare=[news_hash_queue],
            retry=True,
        )


@shared_task
def fresh_news_save(news):
    from news.models import News

    News.objects.create(**news)
