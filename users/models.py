from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'null': True, 'blank': True}


# Create your models here.
class User(AbstractUser):

    username = None
    email = None
    phone_number = models.IntegerField(unique=True, verbose_name='номер')
    verify_code = models.IntegerField(**NULLABLE, verbose_name='код для авторизации')
    referral_code = models.CharField(max_length=6, unique=True, **NULLABLE, verbose_name='реферальный код')
    invite_code = models.CharField(max_length=6, unique=True, **NULLABLE, verbose_name='инвайт код')

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []
# random.randint(1000, 9999)
