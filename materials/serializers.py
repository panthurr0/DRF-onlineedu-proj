from rest_framework.serializers import ModelSerializer, SerializerMethodField
from materials.models import Course, Lesson
from materials.validators import VideoURLValidator


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [VideoURLValidator(field='video_url')]


class CourseSerializer(ModelSerializer):
    lesson_count = SerializerMethodField()
    lesson = LessonSerializer(many=True, read_only=True)

    def get_lesson_count(self, instance):
        return Lesson.objects.filter(course=instance).count()

    class Meta:
        model = Course
        fields = '__all__'
