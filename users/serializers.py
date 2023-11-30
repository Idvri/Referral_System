from rest_framework import serializers

from service.models import ImputedCode

from users.models import User


class UserAuthSerializer(serializers.ModelSerializer):
    number = serializers.IntegerField(min_value=10000000000, max_value=99999999999)

    class Meta:
        model = User
        fields = ('number',)


class UserVerificationSerializer(serializers.ModelSerializer):
    number = serializers.IntegerField(min_value=10000000000, max_value=99999999999)
    verify_code = serializers.IntegerField(min_value=1000, max_value=9999)

    class Meta:
        model = User
        fields = ('number', 'verify_code',)


class UserRetrieveSerializer(serializers.ModelSerializer):
    invite_code = serializers.IntegerField(source='invite_code.code')
    imputed_code = serializers.IntegerField(source='imputed_code.invite_code.code', required=False)
    invited_users = serializers.SerializerMethodField()

    def get_invited_users(self, obj):
        imputed_codes = ImputedCode.objects.filter(invite_code=obj.invite_code.id)
        invited_users = []
        for code in imputed_codes:
            invited_users.extend([user.number for user in code.invited_users.all()])
        return invited_users

    class Meta:
        model = User
        fields = ('number', 'invite_code', 'imputed_code', 'invited_users',)
