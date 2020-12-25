import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class AccountAPITestCase(APITestCase):
    def setUp(self):
        self.user_1 = User.objects.create_user(username='username1', password='password1')
        self.user_2 = User.objects.create_user(username='username2', password='password2')

    def test_create(self):
        self.assertEqual(2, User.objects.all().count())

        url = reverse('account-list')

        data = json.dumps({
            "username": "username3",
            'password': 'password3',
            'password2': 'password3'
        })

        response = self.client.post(url, data=data, content_type='application/json')

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(3, User.objects.all().count())

    def test_delete(self):
        self.assertEqual(2, User.objects.all().count())

        url = reverse("account-detail", args=(self.user_2.id,))

        response = self.client.delete(url)

        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        self.assertEqual(1, User.objects.all().count())
