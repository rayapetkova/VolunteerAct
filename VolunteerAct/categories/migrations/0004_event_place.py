# Generated by Django 5.1.1 on 2024-09-25 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0003_alter_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='place',
            field=models.CharField(max_length=150, null=True),
        ),
    ]