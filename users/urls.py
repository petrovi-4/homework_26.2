from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import UserCreateAPIView, UserUpdateAPIView, UserRetrieveAPIView, UserListAPIView, UserDestroyAPIView, \
    PaymentListAPIView, PaymentCreateAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', UserListAPIView.as_view(), name='user-list'),
    path('create/', UserCreateAPIView.as_view(), name='user-create'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='user-update'),
    path('<int:pk>/', UserRetrieveAPIView.as_view(), name='user-get'),
    path('delete/<int:pk>/', UserDestroyAPIView.as_view(), name='user-delete'),
    path('payment/', PaymentListAPIView.as_view(), name='payment-list'),
    path('payment/create/', PaymentCreateAPIView.as_view(), name='payment-create'),
]
