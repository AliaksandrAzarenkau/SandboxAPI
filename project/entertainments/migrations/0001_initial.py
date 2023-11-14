# Generated by Django 4.2.7 on 2023-11-14 17:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entertainments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_data', models.DateTimeField(default=datetime.datetime(2023, 11, 14, 20, 51, 11, 1095), null=True, verbose_name='Время и дата создания запроса.')),
                ('category', models.CharField(max_length=100, null=True, verbose_name='Категория резвлечения.')),
                ('entertainment', models.CharField(max_length=100, null=True, verbose_name='Развлечение.')),
                ('participants', models.IntegerField(null=True, verbose_name='Количество участников.')),
                ('price', models.FloatField(null=True, verbose_name='Цена.')),
                ('accessibility', models.FloatField(null=True, verbose_name='Доступность.')),
                ('entertainment_id', models.IntegerField(null=True, verbose_name='ID развлечения.')),
                ('link', models.URLField(max_length=100, null=True, verbose_name='Ссылка')),
            ],
        ),
    ]