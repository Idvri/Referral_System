from django.urls import path

from users.apps import UsersConfig
from users.views import PhoneNumberVerificationView, VerifyCodeView

app_name = UsersConfig.name

urlpatterns = [
    path('auth/', PhoneNumberVerificationView.as_view(), name='register'),
    path('auth/token/', VerifyCodeView.as_view(), name='token_obtain_pair'),
]
