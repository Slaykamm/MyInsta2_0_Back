# Generated by Django 4.0.2 on 2022-04-17 13:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0003_alter_author_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(blank=True, upload_to='video/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'mkv'])]),
        ),
    ]
