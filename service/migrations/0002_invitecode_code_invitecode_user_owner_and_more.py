# Generated by Django 4.2.7 on 2023-11-23 15:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitecode',
            name='code',
            field=models.IntegerField(default='318013', verbose_name='Инвайт код'),
        ),
        migrations.AddField(
            model_name='invitecode',
            name='user_owner',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invite_code', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='invitecode',
            name='users_invited',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invited_users', to=settings.AUTH_USER_MODEL),
        ),
    ]