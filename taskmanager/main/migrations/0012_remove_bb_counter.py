# Generated by Django 4.1.2 on 2022-10-30 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_bb_counter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bb',
            name='counter',
        ),
    ]
