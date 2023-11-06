from django.db import models

NULLABLE = {'null': True, 'blank': True}

# Create your models here.
class User(models.Model):
    phone_number = models.CharField(max_length=15, unique=True, verbose_name='номер')
    verify_code = models.CharField(max_length=4, unique=True, **NULLABLE, verbose_name='код для авторизации')
    referral_code = models.CharField(max_length=6, unique=True, **NULLABLE, verbose_name='реферальный код')
    invite_code = models.CharField(max_length=6, unique=True, **NULLABLE, verbose_name='инвайт код')

    class Meta:
        verbose_name = 'Пользователь сервиса'
        verbose_name_plural = 'Пользователи сервиса'