from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Course
from users.models import User


class SubscriptionTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='testik@materials.py')
        self.course = Course.objects.create(course_title='Курс о том', owner=self.user)

        self.client.force_authenticate(user=self.user)

    def test_subscription(self):
        url = reverse('users:sub-create')

        data = {
            'course': self.course.pk
        }

        response_add_message = {
            "message": "Подписка добавлена"
        }

        response_delete_message = {
            "message": "Подписка удалена"
        }

        response = self.client.post(url, data)

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(), response_add_message
        )

        response = self.client.post(url, data)

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(), response_delete_message
        )