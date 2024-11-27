# Generated by Django 5.1.1 on 2024-11-27 09:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0005_alter_appuser_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(max_length=150, null=True, validators=[django.core.validators.MinLengthValidator(2, message='First name needs to be at least 2 characters long.')]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(max_length=150, null=True, validators=[django.core.validators.MinLengthValidator(2, message='Last name needs to be at least 2 characters long.')]),
        ),
    ]
