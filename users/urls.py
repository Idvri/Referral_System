from users.apps import UsersConfig
from django.urls import path

from users.views import UserAuthAPIView, UserVerificationAPIView, UserRetrieveAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('auth/', UserAuthAPIView.as_view(), name='authorization'),
    path('auth/verify/', UserVerificationAPIView.as_view(), name='verification'),

    path('profile/<int:pk>/', UserRetrieveAPIView.as_view(), name='profile'),
]
