from django.contrib import admin

from materials.models import Course, Lesson


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_filter = ("id", "course_title")


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_filter = ("id", "lesson_title")
