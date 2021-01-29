from kombu import Exchange, Queue

news_hash_queue = Queue("news_hash", Exchange("news_hash"), "news_hash")
fresh_news_queue = Queue("fresh_news", Exchange("fresh_news"), "fresh_news")
