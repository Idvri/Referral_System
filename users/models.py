from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from service.models import InviteCode, ImputedCode


# Create your models here.
class User(AbstractUser):
    username = None

    number = models.BigIntegerField(
        validators=[
            MinValueValidator(limit_value=10000000000),
            MaxValueValidator(limit_value=99999999999)
        ],
        unique=True,
        verbose_name='Номер телефона'
    )
    invite_code = models.OneToOneField(
        InviteCode,
        on_delete=models.CASCADE,
        related_name='owner',
    )
    imputed_code = models.ForeignKey(
        ImputedCode,
        on_delete=models.SET_NULL,
        related_name='invited_users',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.number

    USERNAME_FIELD = 'number'
