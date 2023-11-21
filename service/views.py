from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from service.serializers import UserProfileSerializer
from users.models import User


# Create your views here.
class UserProfileAPIView(generics.RetrieveAPIView):
    serializer_class = UserProfileSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
