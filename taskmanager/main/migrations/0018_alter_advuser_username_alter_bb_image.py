# Generated by Django 4.1.2 on 2022-11-14 02:07

import django.core.validators
from django.db import migrations, models
import main.utilities


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_bb_commented_bb_imageses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advuser',
            name='username',
            field=models.CharField(max_length=15, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_username', message='Введите ENGLISH username', regex='^[a-zA-Z]+$')], verbose_name='Имя пользователя'),
        ),
        migrations.AlterField(
            model_name='bb',
            name='image',
            field=models.ImageField(blank=True, upload_to=main.utilities.get_timestamp_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])], verbose_name='Изображение'),
        ),
    ]
