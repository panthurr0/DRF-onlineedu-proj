from rest_framework.serializers import ModelSerializer, SerializerMethodField
from materials.models import Course, Lesson
from materials.validators import VideoURLValidator
from users.models import Subscription


class LessonSerializer(ModelSerializer):
    video_url = [VideoURLValidator(field='video_url')]

    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(ModelSerializer):
    lesson_count = SerializerMethodField()
    is_subscribed = SerializerMethodField()
    lesson = LessonSerializer(many=True, read_only=True)

    def get_lesson_count(self, instance):
        """ Считает количество уроков на курсе """

        return Lesson.objects.filter(course=instance).count()

    def get_is_subscribed(self, instance):
        """ Проверяет наличие подписки на курс у текущего пользователя"""

        if Subscription.objects.filter(course=instance).exists():
            return f'Подписка присутствует'
        else:
            return f'Подписка отсутствует'

    class Meta:
        model = Course
        fields = '__all__'
