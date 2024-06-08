from django.urls import path
from rest_framework.routers import DefaultRouter

from materials.apps import MaterialsConfig
from materials.views import CourseViewSet, LessonCreateApiView, LessonListApiView, LessonRetrieveApiView, \
    LessonUpdateApiView, LessonDestroyApiView

app_name = MaterialsConfig.name

router = DefaultRouter()
router.register('courses', CourseViewSet, basename='courses')

urlpatterns = [
    path('lesson/create', LessonCreateApiView.as_view(), name='lesson-create'),
    path('lesson/', LessonListApiView.as_view(), name='lesson-list'),
    path('lesson/<int:pk>', LessonRetrieveApiView.as_view(), name='lesson-get'),
    path('lesson/update/<int:pk>', LessonUpdateApiView.as_view(), name='lesson-update'),
    path('lesson/delete/<int:pk>', LessonDestroyApiView.as_view(), name='lesson-delete'),

] + router.urls
