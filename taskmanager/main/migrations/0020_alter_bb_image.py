# Generated by Django 4.1.2 on 2022-11-15 06:25

import django.core.validators
from django.db import migrations, models
import main.models
import main.utilities


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_alter_bb_image_alter_bb_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bb',
            name='image',
            field=models.ImageField(blank=True, help_text='Максимальный объем файла не должен превышать 2 МБ', upload_to=main.utilities.get_timestamp_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg', 'bmp']), main.models.validate_image], verbose_name='Изображение'),
        ),
    ]