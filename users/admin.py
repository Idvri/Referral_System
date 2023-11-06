from django.contrib import admin

from users.models import User


# Register your models here.
@admin.register(User)
class User(admin.ModelAdmin):
    list_display = ('phone_number', 'verify_code',)
