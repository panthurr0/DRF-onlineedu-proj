from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import (UserCreateAPIView, UserListAPIView, UserUpdateAPIView, UserRetrieveAPIView,
                         UserDestroyAPIView, PaymentListAPIView, SubscriptionCreateAPIView)

app_name = UsersConfig.name

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='login'),
    path('list/', UserListAPIView.as_view(), name='list'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='update'),
    path('<int:pk>/', UserRetrieveAPIView.as_view(), name='retrieve'),
    path('destroy/<int:pk>/', UserDestroyAPIView.as_view(), name='destroy'),
    path('token/refresh/', TokenRefreshView.as_view(permission_classes=(AllowAny,)), name='token_refresh'),

    path('payment/', PaymentListAPIView.as_view(), name='payment-list'),
    path('subscription/', SubscriptionCreateAPIView.as_view(), name='sub-create')

]
