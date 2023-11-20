from rest_framework import serializers

from users.models import User


class PhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('phone_number',)


class VerifyCodeSerializer(serializers.ModelSerializer):
    verify_code = serializers.IntegerField(min_value=1000, max_value=9999)

    class Meta:
        model = User
        fields = ('phone_number', 'verify_code',)
