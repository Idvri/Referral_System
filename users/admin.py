from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User


# Register your models here.
@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ('phone_number',)
    ordering = ('phone_number',)
