# Generated by Django 2.0.1 on 2018-01-21 07:53

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainsite', '0002_auto_20180115_1212'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='systemuser',
            name='system',
        ),
        migrations.RemoveField(
            model_name='systemuser',
            name='user',
        ),
        migrations.AddField(
            model_name='system',
            name='users',
            field=models.ManyToManyField(related_name='システムユーザ', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='system',
            name='end_date',
            field=models.DateField(blank=True, null=True, verbose_name='終了日'),
        ),
        migrations.AlterField(
            model_name='system',
            name='start_date',
            field=models.DateField(default=datetime.date.today, verbose_name='開始日'),
        ),
        migrations.DeleteModel(
            name='SystemUser',
        ),
    ]
