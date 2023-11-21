from rest_framework import serializers

from users.models import User


class PhoneNumberSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(min_length=11)

    class Meta:
        model = User
        fields = ('phone_number',)


class VerifyCodeSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(min_length=11)
    verify_code = serializers.IntegerField(min_value=1000, max_value=9999)

    class Meta:
        model = User
        fields = ('phone_number', 'verify_code',)
