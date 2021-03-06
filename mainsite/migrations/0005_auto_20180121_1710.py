# Generated by Django 2.0.1 on 2018-01-21 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0004_auto_20180121_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qa',
            name='status',
            field=models.CharField(choices=[('1', '起票'), ('2', '回答完了'), ('3', '確認完了'), ('4', '保留'), ('5', '廃棄')], db_index=True, default='1', max_length=1, verbose_name='ステータス'),
        ),
        migrations.AlterField(
            model_name='qa',
            name='title',
            field=models.CharField(db_index=True, max_length=50, verbose_name='質問概要'),
        ),
        migrations.AlterField(
            model_name='qa',
            name='update_datetime',
            field=models.DateTimeField(auto_now=True, db_index=True, verbose_name='更新日時'),
        ),
    ]
