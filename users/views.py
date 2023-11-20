import random
import time

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import permissions, status

from users.models import User


# Create your views here.
class PhoneNumberVerificationView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        phone_number = request.data.get('phone_number')
        if phone_number and len(phone_number) >= 11:
            verify_code = ''.join(random.choices('0123456789', k=4))
            time.sleep(random.uniform(1, 2))
            request.session['phone_number'] = phone_number
            request.session['verify_code'] = verify_code
            print(verify_code)
            return Response({'detail': f'Код для входа отправлен на номер: {phone_number}.'})
        else:
            return Response({'error': 'Указан неправильный номер телефона!'}, status=status.HTTP_400_BAD_REQUEST)


class VerifyCodeView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        number = request.data.get('phone_number')
        submitted_code = request.data.get('verify_code')
        stored_number = request.session.get('phone_number')
        stored_code = request.session.get('verify_code')
        user = User.objects.filter(phone_number=number).first()
        if int(submitted_code) == int(stored_code) and number == stored_number:
            if not user:
                referral_code = ''.join(random.choices('0123456789', k=6))
                User.objects.create(phone_number=number,  referral_code=referral_code)
            refresh = RefreshToken.for_user(request.user)
            access_token = str(refresh.access_token)
            return Response({'access_token': access_token, 'detail': 'Успешная авторизация!'})
        else:
            return Response({'error': 'Указан неверный код авторизации или номер телефона!'},
                            status=status.HTTP_400_BAD_REQUEST)
