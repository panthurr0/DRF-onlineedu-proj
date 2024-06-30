from rest_framework.generics import (CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView,
                                     DestroyAPIView, get_object_or_404)
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from materials.models import Course, Lesson
from materials.pagination import MaterialsPagination
from materials.serializers import CourseSerializer, LessonSerializer
from materials.tasks import send_notification
from users.permissions import IsModer, IsOwner


class CourseViewSet(ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = MaterialsPagination

    def get_permissions(self):
        if self.action in ["create", "list"]:
            self.permission_classes = [IsAuthenticated | IsModer]
        elif self.action in ["update", "retrieve", "destroy"]:
            self.permission_classes = [IsAuthenticated | IsOwner]
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def update(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        send_notification.delay(course_id=course.id)
        print(f'Курс {course.course_title} обновлён')
        return super().update(request)


class LessonCreateApiView(CreateAPIView):
    serializer_class = LessonSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LessonListApiView(ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    pagination_class = MaterialsPagination


class LessonRetrieveApiView(RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsModer | IsOwner, IsAuthenticated]


class LessonUpdateApiView(UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsModer | IsOwner, IsAuthenticated]


class LessonDestroyApiView(DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner, IsAuthenticated]
