from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'null': True, 'blank': True}


# Create your models here.
class User(AbstractUser):

    username = None
    phone_number = models.CharField(unique=True, verbose_name='Номер')
    referral_code = models.IntegerField(unique=True, verbose_name='Реферальный код', **NULLABLE)
    invite_code = models.IntegerField(unique=True, verbose_name='Инвайт код', **NULLABLE)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
