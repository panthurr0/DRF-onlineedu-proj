from rest_framework import serializers

from materials.models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'course_title', 'course_description')
