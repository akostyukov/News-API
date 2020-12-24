import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from news.models import News
from news.serializers import NewsSerializer


class NewsAPITestCase(APITestCase):
    def setUp(self):
        self.news_1 = News.objects.create(category='Криминал', header='Заголовок 1 новости', text='Текст 1 новости')
        self.news_2 = News.objects.create(category='Культура', header='Заголовок 2 новости', text='Текст 2 новости')

    def test_get(self):
        url = reverse('news-list')
        response = self.client.get(url)
        data = NewsSerializer([self.news_1, self.news_2], many=True).data

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(data, response.data)

    def test_create(self):
        self.assertEqual(2, News.objects.all().count())

        url = reverse('news-list')

        data = json.dumps({
            'category': 'Из жизни',
            'header': 'Заголовок новости из жизни',
            'text': 'Текст новости из жизни'
        })

        response = self.client.post(url, data=data, content_type='application/json')

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(3, News.objects.all().count())

    def test_update(self):
        url = reverse('news-detail', args=(self.news_1.id,))

        data = json.dumps({
            'category': self.news_1.category,
            'header': 'Абсолютно новый заголовок',
            'text': self.news_1.text
        })

        response = self.client.put(url, data, content_type='application/json')

        self.news_1.refresh_from_db()

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual('Абсолютно новый заголовок', self.news_1.header)

    def test_delete(self):
        self.assertEqual(2, News.objects.all().count())

        url = reverse('news-detail', args=(self.news_2.id,))

        response = self.client.delete(url)

        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        self.assertEqual(1, News.objects.all().count())
