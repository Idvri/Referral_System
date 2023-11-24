import random
import time

from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken

from users.models import User
from users.permissions import IsOwner
from users.serializers import UserAuthSerializer, UserVerificationSerializer, UserRetrieveSerializer

from service.models import InviteCode, ImputedCode


# Create your views here.
class UserAuthAPIView(APIView):
    serializer_class = UserAuthSerializer

    def post(self, request):
        number = int(request.data.get('number'))
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid() and not User.objects.filter(number=number).first():
            return Response({'number': 'Указан неправильный номер телефона!'}, status=status.HTTP_400_BAD_REQUEST)

        verify_code = int(InviteCode.get_code()[:4])
        request.session['user'] = {'number': number, 'verify_code': verify_code}
        time.sleep(random.uniform(1, 2))
        print(verify_code)
        return Response({'detail': f'Код для входа отправлен на номер: {number}.'})


class UserVerificationAPIView(APIView):
    serializer_class = UserVerificationSerializer

    def post(self, request):
        user = {'number': int(request.data.get('number')), 'verify_code': int(request.data.get('verify_code'))}
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid() and not User.objects.filter(number=user['number']).first() or \
                user != request.session.get('user') or not request.session.get('user'):
            return Response(
                {'number_or_verify_code': 'Указан неправильный номер телефона или код для входа!'},
                status=status.HTTP_400_BAD_REQUEST
            )

        user_auth = User.objects.filter(number=user['number']).first()

        if not user_auth:
            number = user['number']
            invite_code = InviteCode.objects.create(code=InviteCode.get_code())
            user_auth = User.objects.create(number=number, invite_code=invite_code)

        request.user = user_auth
        access_token = AccessToken.for_user(request.user)
        request.session.clear()
        return Response(
            {'access_token': str(access_token), 'detail': 'Успешная авторизация!'},
            status=status.HTTP_200_OK
        )


class UserRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = UserRetrieveSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]

    def post(self, request, pk):
        referral_code = request.data.get('referral_code')
        if not referral_code:
            return Response({'referral_code': 'Не указан инвайт-код!'}, status=status.HTTP_400_BAD_REQUEST)

        referral_code = int(referral_code)
        user = User.objects.get(pk=pk)
        invite_code = InviteCode.objects.filter(code=referral_code).first()
        if not invite_code:
            return Response({'referral_code': 'Указан недействительный инвайт-код!'}, status=status.HTTP_400_BAD_REQUEST)

        if user.invite_code.code == referral_code:
            return Response(
                {'referral_code': 'Нельзя указывать свой собственный инвайт-код!'},
                status=status.HTTP_400_BAD_REQUEST
            )

        if user.imputed_code:
            return Response({'referral_code': 'Вы уже вводили инвайт-код!'}, status=status.HTTP_400_BAD_REQUEST)

        input_code = ImputedCode.objects.create(invite_code=invite_code)
        user.imputed_code = input_code
        user.save()
        return Response(
            {'detail': f'Вы успешно ввели инвайт-код пользователя "{invite_code.owner.number}"!'},
            status=status.HTTP_200_OK
        )
