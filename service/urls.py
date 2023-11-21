from django.urls import path

from service.apps import ServiceConfig
from service.views import UserProfileAPIView

app_name = ServiceConfig.name

urlpatterns = [
    path('profile/<int:pk>', UserProfileAPIView.as_view(), name='profile'),
]
