from datetime import date

from django.core.management import BaseCommand

from materials.models import Course, Lesson, Payment
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        courses_list = [
            {'course_title': 'English', 'course_description': 'to level advanced'},
            {'course_title': 'Programming', 'course_description': 'python'},
            {'course_title': 'Math', 'course_description': 'quick math in mind'}
        ]
        lessons_list = [
            {'lesson_title': 'Simples', 'lesson_description': 'Present and past', 'course': 1},
            {'lesson_title': 'Loops', 'lesson_description': 'for', 'course': 2},
            {'lesson_title': 'Plus', 'lesson_description': '2+2', 'course': 3},
            {'lesson_title': 'Integers', 'lesson_description': '1', 'course': 2},
        ]

        users_list = [
            {'email': 'bla@mail.ru'},
            {'email': 'test@mail.ru'},
            {'email': 'some@mail.ru'},
        ]

        payments_list = [
            {'user': 1, 'course': 1, 'pay_sum': 1000, 'pay_method': Payment.CASH, 'pay_date': date(2020, 5, 5)},
            {'user': 2, 'lesson': 1, 'pay_sum': 500, 'pay_method': Payment.TRANSFER, 'pay_date': date(2023, 1, 1)},
        ]

        course_for_create = []
        for course_item in courses_list:
            course_for_create.append(
                Course(**course_item)
            )
        Course.objects.bulk_create(course_for_create)

        lesson_for_create = []
        for lesson_item in lessons_list:
            lesson_item['course'] = Course.objects.get(id=lesson_item['course'])
            lesson_for_create.append(
                Lesson(**lesson_item)
            )
        Lesson.objects.bulk_create(lesson_for_create)

        user_for_create = []
        for user_item in users_list:
            user_for_create.append(
                User(**user_item)
            )
        User.objects.bulk_create(user_for_create)

        payment_for_create = []
        for payment_item in payments_list:
            payment_item['user'] = User.objects.get(id=payment_item['user'])
            if 'course' in payment_item:
                payment_item['course'] = Course.objects.get(id=payment_item['course'])
            if 'lesson' in payment_item:
                payment_item['lesson'] = Lesson.objects.get(id=payment_item['lesson'])
            payment_for_create.append(
                Payment(**payment_item)
            )
        Payment.objects.bulk_create(payment_for_create)