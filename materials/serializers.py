from rest_framework import serializers

from materials.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lessons = serializers.SerializerMethodField()

    def get_lesson_count(self, instance):
        return Lesson.objects.filter(course=instance).count()

    def get_lessons(self, instance):
        lessons = Lesson.objects.filter(course=instance)
        return LessonSerializer(lessons, many=True).data

    class Meta:
        model = Course
        # fields = ('id', 'course_title', 'course_description',
        #           'lesson_count', 'lesson')
        fields = '__all__'
