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
        self.response_add_message = {'message': 'Подписка добавлена'}
        self.response_delete_message = {'message': 'Подписка удалена'}

    def _test_subscription_helper(self, expected_response):
        url = reverse('users:sub-create')
        data = {
            'course': self.course.pk
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), expected_response)

    def test_subscription(self):
        self._test_subscription_helper(self.response_add_message)
        self._test_subscription_helper(self.response_delete_message)
