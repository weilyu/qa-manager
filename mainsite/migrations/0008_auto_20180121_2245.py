# Generated by Django 2.0.1 on 2018-01-21 13:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0007_system_manager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='system',
            name='users',
            field=models.ManyToManyField(null=True, related_name='システムユーザ', to=settings.AUTH_USER_MODEL),
        ),
    ]
