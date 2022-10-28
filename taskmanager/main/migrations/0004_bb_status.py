# Generated by Django 4.1.2 on 2022-10-28 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_bb_additionalimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='bb',
            name='status',
            field=models.CharField(choices=[('new', 'новый'), ('confirmed', 'подвтрежденный'), ('canceled', 'отмененный')], default='new', max_length=254, verbose_name='Статус'),
        ),
    ]
