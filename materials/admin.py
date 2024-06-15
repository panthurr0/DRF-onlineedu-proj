from django.contrib import admin

from materials.models import Course, Lesson, Payment


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_filter = ("id", "course_title")


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_filter = ("id", "lesson_title")


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_filter = ("id", "user", "course", "lesson", "pay_method")
