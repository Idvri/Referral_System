from rest_framework import serializers

from service.models import ImputedCode

from users.models import User


class UserAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('number',)


class UserVerificationSerializer(serializers.ModelSerializer):
    verify_code = serializers.IntegerField(min_value=1000, max_value=9999)

    class Meta:
        model = User
        fields = ('number', 'verify_code',)


class UserRetrieveSerializer(serializers.ModelSerializer):
    invite_code = serializers.IntegerField(source='invite_code.code')
    imputed_code = serializers.IntegerField(source='imputed_code.invite_code.code', required=False)
    invited_users = serializers.SerializerMethodField()

    def get_invited_users(self, obj):
        code = ImputedCode.objects.filter(invite_code=obj.invite_code.id).first()
        if code:
            return [user.number for user in code.invited_users.all()]
        return []

    class Meta:
        model = User
        fields = ('number', 'invite_code', 'imputed_code', 'invited_users',)
