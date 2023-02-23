from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from datetime import datetime


class EventTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.token = Token.objects.create(user=self.user)

    def test_create_event(self):
        self.client.force_authenticate(user=self.user, token=self.token.key)
        url = '/create/'
        data = {
            "event_type": "test_event",
            "info": {"key1": "value1", "key2": "value2"},
            "timestamp": str(datetime.now())
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_event_unauthenticated(self):
        url = '/create/'
        data = {
            "event_type": "test_event",
            "info": {"key1": "value1", "key2": "value2"},
            "timestamp": str(datetime.now())
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
