from django.urls import reverse

from rest_framework.authtoken.admin import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIClient
from rest_framework import status


class EventPostTest(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123')
        self.token = Token.objects.create(user=self.user)
        client = APIClient()
        client.credentials(HTTP_AUTORIZATION=self.token)

    def test_post_event_no_auth(self):
        simple_event = {"event_type": "test_name", "info": "json", "timestamp": "2023-02-06 14:05:50"}
        response = self.client.post(reverse('event'), simple_event)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_event_auth(self):
        simple_event = {"event_type": "test_name", "info": "json", "timestamp": "2023-02-06 14:05:50"}
        response = self.client.post(reverse('event'), simple_event,
                                    headers={'Authorization': 'Token ' + self.token.key})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
