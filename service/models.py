import random

from django.db import models


# Create your models here.
class InviteCode(models.Model):
    code = models.IntegerField(
        unique=True,
        verbose_name='Инвайт код',
    )

    def __str__(self):
        return self.code

    @staticmethod
    def get_code():
        return ''.join(str(random.randint(100000, 999999)))

    class Meta:
        verbose_name = 'Инвайт код'


class ImputedCode(models.Model):

    invite_code = models.ForeignKey(
        InviteCode,
        on_delete=models.CASCADE,
        related_name='invited_users',
    )

    def __str__(self):
        return self.invite_code

    class Meta:
        verbose_name = 'Введённый код'
