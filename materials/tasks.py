from celery import shared_task
from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER
from materials.models import Course
from users.models import Subscription


@shared_task
def send_notification(course_id: int) -> str:
    """Отправляет письмо подписчикам о редактировании материалов курса"""
    course = Course.objects.get(pk=course_id)
    subs = Subscription.objects.filter(course=course_id)

    emails_sent = 0
    for sub in subs:
        emails_sent += 1
        send_mail(
            "Уведомление об изменениях в материалах курса",
            f"Курс {course.course_title} изменился",
            EMAIL_HOST_USER,
            [sub.user.email],
        )

    return f"Было отправлено {emails_sent} писем"
