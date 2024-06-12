from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    course_title = models.CharField(
        verbose_name='Название курса',
        max_length=75
    )

    course_description = models.TextField(
        verbose_name='Описание',
        **NULLABLE
    )

    image = models.ImageField(
        upload_to="materials/course",
        verbose_name='Превью(картинка)',
        **NULLABLE
    )

    def __str__(self):
        return f'{self.course_title}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    lesson_title = models.CharField(
        verbose_name='Название урока',
        max_length=75
    )
    lesson_description = models.TextField(
        verbose_name='Описание урока',
        **NULLABLE
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

    def __str__(self):
        return f'{self.lesson_title} из курса {self.course}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
