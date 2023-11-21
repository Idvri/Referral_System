from django.db import models


# Create your models here.
class Helo(models.Model):
    name = models.CharField(default='nice')
