from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from materials.models import Course, Lesson
from users.models import User


class MaterialsTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(email='testik@materials.py')
        self.course = Course.objects.create(course_title='Курс о том', owner=self.user)
        self.lesson = Lesson.objects.create(lesson_title='Урок о том', course=self.course, owner=self.user)

        self.client.force_authenticate(user=self.user)

    def test_course_retrieve(self):

        url = reverse('materials:courses-detail', args=(self.course.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )

        self.assertEqual(
            data.get('course_title'), self.course.course_title
        )

    def test_course_create(self):

        url = reverse('materials:courses-list')
        data = {
            'course_title': 'Курс такойто'
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )

        self.assertEqual(
            Course.objects.all().count(), 2
        )

    def test_course_update(self):

        url = reverse('materials:courses-detail', args=(self.course.pk,))
        data = {
            'course_title': 'Курс такойто'
        }
        response = self.client.patch(url, data)
        response_data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )

        self.assertEqual(
            response_data.get('course_title'), 'Курс такойто'
        )

    def test_course_delete(self):

        url = reverse('materials:courses-detail', args=(self.course.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Course.objects.all().count(), 0
        )

    def test_course_list(self):

        url = reverse('materials:courses-list')
        response = self.client.get(url)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
