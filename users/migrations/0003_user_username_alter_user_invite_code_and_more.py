# Generated by Django 4.2.7 on 2023-11-19 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_options_alter_user_invite_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=11, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='invite_code',
            field=models.IntegerField(blank=True, null=True, unique=True, verbose_name='Инвайт код'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=11, unique=True, verbose_name='Номер'),
        ),
        migrations.AlterField(
            model_name='user',
            name='referral_code',
            field=models.IntegerField(blank=True, null=True, unique=True, verbose_name='Реферальный код'),
        ),
        migrations.AlterField(
            model_name='user',
            name='verify_code',
            field=models.IntegerField(verbose_name='Код для авторизации'),
        ),
    ]
