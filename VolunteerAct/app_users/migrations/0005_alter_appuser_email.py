# Generated by Django 5.1.1 on 2024-11-18 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0004_alter_profile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='email',
            field=models.EmailField(error_messages={'unique': 'User with this email already exists.'}, max_length=254, unique=True),
        ),
    ]
