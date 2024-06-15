from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    course_title = models.CharField(
        verbose_name='Название курса', max_length=75
    )

    course_description = models.TextField(
        verbose_name='Описание', **NULLABLE
    )

    image = models.ImageField(
        upload_to="materials/course",
        verbose_name='Превью(картинка)',
        **NULLABLE
    )

    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        **NULLABLE,
        verbose_name='владелец'
    )

    def __str__(self):
        return f'{self.course_title}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    """
    В одном курсе :model:`materials.Course` может быть много уроков
    """
    lesson_title = models.CharField(
        verbose_name='Название урока', max_length=75
    )

    lesson_description = models.TextField(
        verbose_name='Описание урока', **NULLABLE
    )

    lesson_image = models.ImageField(
        upload_to="materials/lesson",
        verbose_name='Превью(картинка) урока',
        **NULLABLE
    )

    video_url = models.CharField(
        verbose_name='Ссылка на видео',
        max_length=200,
        **NULLABLE
    )

    course = models.ForeignKey(
        Course,
        verbose_name='Курс',
        on_delete=models.SET_NULL,
        **NULLABLE,
        related_name='lesson'
    )

    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        **NULLABLE,
        verbose_name='Владелец'
    )

    def __str__(self):
        return f'{self.lesson_title} из курса {self.course}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class Payment(models.Model):
    TRANSFER = 'Перевод'
    CASH = 'Наличные'

    PAYMENT_METHODS = [
        (TRANSFER, 'Перевод на счёт'),
        (CASH, 'Наличными'),
    ]

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, **NULLABLE
    )

    pay_date = models.DateField(
        verbose_name='Дата оплаты', **NULLABLE
    )

    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, **NULLABLE
    )

    lesson = models.ForeignKey(
        Lesson, on_delete=models.CASCADE, **NULLABLE
    )

    pay_sum = models.PositiveIntegerField(
        verbose_name='Сумма оплаты'
    )

    pay_method = models.CharField(
        verbose_name='Способ оплаты',
        choices=PAYMENT_METHODS,
        default=TRANSFER
    )

    def __str__(self):
        return (f'{self.user}: {self.pay_method}.'
                f'{self.course if self.course else self.lesson}')

    class Meta:
        verbose_name = 'Оплата'
        verbose_name_plural = 'Оплаты'
